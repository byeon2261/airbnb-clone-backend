패키지 설치 및 관리를 위해 poetry를 사용한다.(=pip) pip보다 관계관리에 편리하다.
poetry를 설치한다. (https://python-poetry.org/docs)
$ curl -sSL https://install.python-poetry.org | python3 -
그리고 터미널을 죽인 후에 터미널을 다시 열고 poetry를 실행시킨다. (vscode에선 쓰래기통 아이콘을 클릭해서 kill terminal 할 수 있다.)

가상환경(shell)을 생성하여 shell내에 django를 설치해준다. 컴퓨터 전역에 django를 설치하지 않기위해서다.

poetry를 설치해준다.
$ poetry init
    여러 질문형식으로 값을 넣어주면 알아서 설정해준다.
    전부 엔터를 쳐주고 마지막에 no no yes를 넣어준다.(라이센스는 MIT)
pyproject.toml 파일이 생성되며 설정내용은 구현되어있다.

poetry를 통해 django를 설치한다.
$ poetry add django
poetry.lock이 생성된다. 코드가 실행된 환경에 대한 정보를 담고 있다.
poetry.toml tool부분에 django내용이 추가된다.
    poetry.lock, poetry.toml 파일을 읽어서 shell이 만들어 진다.

poetry shell안에서 django를 사용 가능하다.
poetry shell안으로 들어간다. (django 는 airbnb-clone-backend 폴더 안에 만든 poetry 방울 안에만 설치되어 있다!)
$ poetry shell   

django사용가능하여, 명령어를 확인 가능하다.
$ django-admin

프로젝트를 실행해준다. 보통은 프로젝트생성하면서 디렉토리도 같이 생성하지만 poetry초기화를 위해서 미리 디렉토리를 생성했다.
$ django-admin startproject [프로젝트명='config'] .
프로젝트 폴더와 manage.py 이 생성된다. manage.py 파일이 터미널에서 Django 명령어를 실행한다.
    $ python manage.py [tap]   을 클릭하면 실행가능한 명령어들을 확인 할 수 있다.

서버를 실행해본다. 
$ python manage.py runserver
데이터베이스가 없다면 db.sqlite3 가 생성된다. 
서버는 실행이되나 migration을 해달라는 경고문이 발생한다.

./admin 에 접속을 하면 no such table: django_session 에러가 발생한다. 
admin 패널을 실행하기 위해서는 admin 유저가 필요하며 admin 유저가 작동하기 위해서는 session이 필요하다.
    이렇게 Django에는 admin패널을 위한 기능이 내장되어 있다.
해당 session을 생성하기 위해서는 migrate가 필요하다.
$ python manage.py migrate
db에 app 데이터가 추가되었다. 마이그래이션 파일은 데이터베이스의 모양을 변형시키는 파이선코드가 들어있다.

python 서버를 실행시키며 터미널을 하나 더 실행시킨 후 shell안에서 admin user를 생성한다.
$ python manage.py createsuperuser
admin user 가 생성되면 로그인이 되며 user리스트에서 추가된것을 확인 가능하다. 데이터 변경에 정적이지 않으며 실시간 동작한다. 
functional하게 실행된며 유저인증도 쉽게 얻을 수 있다. 유저정보 변경 및 권한 변경도 패널에서 가능하다. awesome!
비밀번호는 hash화 되어 저장되면 원본 비밀번호는 저장되지 않는다. 유저가 생성된 날짜와 마지막 접속일자도 확인 가능.
user 패널은 리스트 컬럼명과 filter기능이 기본 구현되어있다.

라이브러리는 코드에서 해당 라이브러리를 request하여 사용하지만 프레임워크는 프레임워크에서 내 코드를 찾아서 실행한다. 프레임워크가 요구하는 위치에 코드가 있어야 실행이 된다.

app 내에 시간은 세계시간(UTC)기준으로 표기된다. config>settings.py 변경해준다.
    TIME_ZONE = "UTC"
    >>>TIME_ZONE = "Asia/Seoul"
언어도 변경해준다.
    LANGUAGE_CODE = "en-us"
    >>>LANGUAGE_CODE = "ko-kr"

config>url.py 은 url path, 실행될 app을 구현한다.
settings.py, urls.py 파일명과 구현된 variable은 프레임워크 요건에 충족시켜야 실행된다.

장고 app 은 어플리케이션의 로직과 데이터를 합쳐서 캡슐화한다.


    #### 4. Django Apps

house 엡을 생성한다.
$ python manage.py startapp houses
    [app]> migrations폴더, __init.py, admin.py, apps.py, models.py, tests.py, views.py 생성된다.
각 파일에는 구현해야할 코드가 무엇인지 주석이 있다.

config>settings.py 에 INSTALLED_APPS 리스트에 앱을 추가하여 설치한다.
    "houses.apps.HousesConfig",
추가를 해주면 설치가 완료되며 django가 해당 app을 인지한다.

models.py엔 app 에 데이터형태를 구현한다. 구현된 형태를 migration 하면 django 는 database를 만들어준다.
model을 구현할때 djanog의 models.Model을 overriding한다. 
    CharField : 최대길이값이 필수 (max_length)
    PositiveIntegerField : 양수인 정수값만 받음

Django 는 커스텀 데이터에 대한 관리 패널을 자동으로 생성해준다. admin.py에 해당 앱 관리에 추가해준다.
    from .models import House
    
    @admin.register(House)  # admin(통제)할 앱을 넣어준다. 여러개 넣을 수 있다.
    class HouseAdmin(admin.ModelAdmin):  # ModelAdmin 은 admin패널이다.
        # admin 패널 화면 구현
        pass
pass로 overriding 하면 구현된 model을 전부 넣어준다.

해당 app을 데이터베이스에 알려줘야한다. 데이터베이스에 모델을 생성해준다.
$ python manage.py makemigrations
    [app]>migrations 폴더에 새로운 db 모델을 설명하는 파일이 생성된다.
그리고 migrate를 실행하여 데이터베이스의 모양을 update한다.
    __pycache__폴더에 변경된 데이터를 설명하는 파일이 생성된다.

    # 도중에 `db.sqlite3`파일을 지워서 migrate해도 no such table이 뜨신다면,
    # $ python manage.py migrate --run-syncdb

서버를 실행하여 앱 admin패널에서 데이터 검색, 추가, 수정, 삭제가 가능하다. django는 데이터 저장 및 수정에서 데이터 유효검사를 해준다.

settings.py 에 INSTALLED_APPS 을 SYSTEM_APPS와 CUSTOM_APPS로 분류 적용한다.
    INSTALLED_APPS = SYSTEM_APPS + CUSTOM_APPS
Django 에서 INSTALLED_APPS 를 찾는다.

