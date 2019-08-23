# PDF HORIZON CROPPER

이 프로그램은 장당 2쪽으로 구성된 PDF를 쉽게 분할하기 위해 만들어진 파이썬 프로그램입니다.

## 사용 요구 사항

1. pip install pypdf2

## 사용 방법

1. original_pdf 폴더에 자르고 싶은 PDF를 모두 넣습니다.
2. python pdfHorizonCropper.py로 프로그램을 실행합니다.

## 기능 추가(앞표지, 뒷표지 자르기)

1. 책의 규격이 188*257인 경우 표지 파일(표1~표4) PDF를 이용해 앞표지, 뒷표지 PDF를 만들 수 있습니다.

### 사용 방법

1. coverOriginal_pdf 폴더에 표지를 넣습니다.
2. python pdfBackCoverCropper.py 또는 python pdfFrontCoverCropper.py로 프로그램을 실행합니다.