# Image_Gallery API
## How to use: 
### create account:
  you can create account with a POST request on img-gallery.up.railway.app/users/register/ 
  with in the body (key:value) the key are:  email, date_of_birth, password, password2 

### login account:
  you can recive your token with a POST request on img-gallery.up.railway.app/users/login/
  with in the body (key:value) the key are:  email, password

### change-password: 
  you can change your password with a POST request on img-gallery.up.railway.app/users/change-password/
  in the header you need to add your token (key:value): authorizon : Bearer    your-token  
  and in the body (key:value) the key are: current_password, new_password 

### upload_img: 
   you can upload img with a POST request on img-gallery.up.railway.app/upload_img/
   in the header you need to add your token (key:value): authorizon : Bearer    your-token  
   and in the body (key:value) the key are: image (the img need to be coded in base64) , title

### download_img: 
   you can upload img with a GET request on img-gallery.up.railway.app/download_img/<int:id>/
   in the header you need to add your token (key:value): authorizon : Bearer    your-token  
  
### image_list: 
  you can see all your images with a GET request on img-gallery.up.railway.app/images_list/
  in the header you need to add your token (key:value): authorizon : Bearer    your-token

### delete_img:
   you can upload img with a DELETE request on img-gallery.up.railway.app/delete_img/<int:id>/
   in the header you need to add your token (key:value): authorizon : Bearer    your-token
   

## example:
### authorizon:
![image](https://github.com/BrunoMartelli01/Image_Gallery/assets/47886680/d59e5b0c-00f9-4a8a-bb5e-97515cd4495e)
### login:
![image](https://github.com/BrunoMartelli01/Image_Gallery/assets/47886680/5ed3ba99-c426-4330-b953-c79101fc437c)
### upload_img:
![image](https://github.com/BrunoMartelli01/Image_Gallery/assets/47886680/4bdd166a-6093-4baf-accd-81177636b6b2)
