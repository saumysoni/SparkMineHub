from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
import requests
from django.contrib.auth.decorators import login_required
import boto3


@login_required
def post_list(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'posts/post_list.html', {'posts': posts})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # Call the profanity check API for title
            title_response = requests.post("http://34.203.214.188:8081/check-profanity", json={'text': post.title})
            
            
            if title_response.status_code == 200:
                title_inappropriate = title_response.json().get('contains_profanity', False)
                if title_inappropriate:
                    error_msg = "Inappropriate post title. Please check and re-enter!"
                    return render(request, 'posts/post_create.html', {'form': form, 'error_msg': error_msg})
                else:
                    # Call the profanity check API for content
                    response = requests.post("http://34.203.214.188:8081/check-profanity", json={'text': post.content})
                    if response.status_code == 200:
                        contains_profanity = response.json().get('contains_profanity', False)
                        contains_profanity = False
                        if contains_profanity:
                            error_msg = "Inappropriate text content. Please check and re-enter!"
                            return render(request, 'posts/post_create.html', {'form': form, 'error_msg': error_msg})
                        else:
                            # Call the Relevance Check API
                            relevance_response = response = requests.post("http://34.203.214.188:8082/classify", json={'text': post.content})
                            if relevance_response.status_code == 200:
                                is_irrelevant = relevance_response.json().get('result',False)
                                is_irrelevant = True
                                if not is_irrelevant:
                                    error_msg = "Irrelevant Information. Please post content related to mining!"
                                    return render(request, 'posts/post_create.html', {'form': form, 'error_msg': error_msg})
                                else:
                                    for filename in request.FILES:
                                        file = request.FILES[filename]
                                        file_name = file.name
                                    s3 = boto3.client('s3', aws_access_key_id="************", aws_secret_access_key="***************", region_name="us-east-1")
                                    bucket_name = 'minehub1'
                                    s3.upload_fileobj(file, bucket_name, file_name)

                                    # Call the Image Appropriateness API
                                    response_img = requests.post("http://34.203.214.188:8080/check-image", json={'bucket_name': 'inappropriatebucket','object_key':file_name})
                                    if response_img.status_code == 200:
                                    
                                        if response_img.json().get('inappropriate_content_detected'):
                                            s3.delete_object(Bucket=bucket_name, Key=file_name)
                                            error_msg = "Inappropriate Image !!"
                                            return render(request, 'posts/post_create.html', {'form': form, 'error_msg': error_msg})
                                        else:
                                            post.author = request.user
                                            post.save()
                                            return redirect('home')
                                    else:
                                        error_msg = "Error checking image. Please try again later."
                                        return render(request, 'posts/post_create.html', {'form': form, 'error_msg': error_msg})
                    else:
                        error_msg = "Error checking content for profanity. Please try again later."
                        return render(request, 'posts/post_create.html', {'form': form, 'error_msg': error_msg})        
                
            else:   
                error_msg = "Error checking title for profanity. Please try again later."
                return render(request, 'posts/post_create.html', {'form': form, 'error_msg': error_msg})
            
    else:
        form = PostForm()
    
    return render(request, 'posts/post_create.html', {'form': form})