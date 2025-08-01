# django_2025

# django 프로젝트
django 기반 블로그 제작 프로젝트입니다.
## 🛠 사용 기술

- **언어**: Python 3.13.5 
- **프레임워크**: Django 5.2.4  
- **데이터베이스**: SQLite3  

## 🧩 주요 앱 설명

- **blog**: 게시글 작성, 조회, 카테고리 분류 기능  
- **library**: 도서 목록 출력 및 관리 기능  
- **single_pages**: 소개 및 정적 페이지 구성


## ✅ 주요 기능

- ✅ 글 목록 조회
- ✅ 글 상세 보기
- ✅ 카테고리별 보기
- ❌ 댓글 기능 (추가 예정)

## 🚀 실행 방법

```bash
git clone https://github.com/your-id/project-name.git
cd project-name
python manage.py runserver

---

## 주요 화면

### 🏠 메인 화면
- 전체 글 목록을 보여줍니다.
![blog 메인](../docs/images/blog_main.png)

### 🗂️ 카테고리 목록 화면
- 등록된 카테고리 리스트를 보여줍니다.
![blog 카테고리 목록](../docs/images/blog_category_list.png)

### 📚 카테고리별 글 목록 화면
- 선택한 카테고리에 속한 글만 보여줍니다.
![blog 카테고리 상세](../docs/images/blog_category_detail.png)

### 📝 글 상세 화면
- 글의 제목, 내용, 작성일을 확인할 수 있습니다.
![blog 글 상세](../docs/images/blog_detail.png)
