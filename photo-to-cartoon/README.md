# Photo-to-Cartoon
This is a photo-to-cartoon converter using openCV

- **Photo-to-Cartoon**
  - [cartoon.py](https://github.com/yubin0727/vision-paint/blob/main/photo-to-cartoon/cartoon.py)
  - using Laplacian to detect edges
  - ChatGPT가 제안한 코드 [cartoon_gpt.py](https://github.com/yubin0727/vision-paint/blob/main/photo-to-cartoon/cartoon_gpt.py)
  - 결과물 비교(ChatGPT - right, down) / 사진 모두 직접 촬영
    - 둘 다 밝거나 색 변화가 뚜렷한 이미지에서 더 만화같아 보임
    - cartoon.py가 cartoon_gpt.py보다 더 디테일하게 표현
    - cartoon_gpt.py가 cartoon.py보다 edge를 더 강하게 표현
    
    <img src = "https://user-images.githubusercontent.com/101437398/228599395-64fd23c0-52a3-462e-9f58-a3c04e4e82b5.jpg" width="70%" height="70%">
    
    <img src = "https://user-images.githubusercontent.com/101437398/228599741-d9c98a27-21d3-4e13-baa0-812de81c7fc8.jpg" width="70%" height="70%">
    
    <img src = "https://user-images.githubusercontent.com/101437398/228599812-36ec7673-aa87-47f4-840b-3b6510ac8a6f.jpg" width="70%" height="70%">
    
    <img src = "https://user-images.githubusercontent.com/101437398/228599921-409844d0-039d-4591-85ed-3114dce90bf7.jpg" width="70%" height="70%">
    
