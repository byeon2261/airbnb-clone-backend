[1_python]

    일부 운영체제에서는 호환성때문에 python명령어를 사용하면 python2로 접속이 된다. python2는 사용하면 안되며 python3를 사용해야 한다.
    $ python3

    git을 생성 및 초기화
    $ git init

[2_Django]

    패키지 설치 및 관리를 위해 poetry를 사용한다.(=pip) pip보다 관계관리에 편리하다.
    poetry를 설치한다.

<https://python-poetry.org/docs>

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

## 4. Django Apps

#### [2_Django]

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
        다른 설정 방법 확인은

<https://docs.djangoproject.com/en/4.1/ref/models/fields/>
primarykey, unique, verbose_name

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

    # 도중에 `db.sqlite3`파일을 지워서 migrate해도 no such table이 뜬다면,
    # $ python manage.py migrate --run-syncdb

    서버를 실행하여 앱 admin패널에서 데이터 검색, 추가, 수정, 삭제가 가능하다. django는 데이터 저장 및 수정에서 데이터 유효검사를 해준다.

    settings.py 에 INSTALLED_APPS 을 SYSTEM_APPS와 CUSTOM_APPS로 분류 적용한다.
        INSTALLED_APPS = SYSTEM_APPS + CUSTOM_APPS
    Django 에서 INSTALLED_APPS 를 찾는다.

#### [1_python]

    models.py에 __str__을 구현하여 해당 app 데이터를 불러올때 표시할 값을 정한다.
        def __str__(self):
            return self.name

#### [2_Django]

    admin.py에 admin패널 리스트 컬럼과 필터를 적용할 수 있다. string으로 리스트에 추가한다.
        list_display = [
            # 리스트에 표기할 컬럼(variable)
        ]
        list_filter = [
            # 필터에 추가할 variable
        ]

    # 예전에 makemigrations 이 없을 때에는 db를 삭제하고 새로 생성했어야했다.

    admin패널에서 검색창을 구현할 수 있다. string으로 리스트에 추가한다.
        search_fields = [
            # 검색할 var
        ]
    리스트에 추가된 variable 내에서 조회가 이뤄진다.
    기본 설정으로는 검색값의 string 이 포함된 전체 컬럼을 조회해온다. 조회될 값을 찾는 방법을 설정할 수 있다.
        [variable]__startswith : 검색값으로 시작하는 값을 조회
        그외의 설정방법은

<https://docs.djangoproject.com/en/4.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields>
exclude, fields, list_display_links, list_per_page, list_editable, read_only ....

## 5. Users App

#### [2_Django]

    Django에는 기본 user관리를 위한 데이터테이블과 admin판넬이 제공된다. 하지만 user 데이터 변경을 위해서는 Django의 user클래스를 inherit하여 overriding을 할 필요가 있다.

<https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#substituting-a-custom-user-model>

    데이터 작업이 어느정도 이뤄지고 나서 users app을 변경할려면 작업이 매우 복잡해진다. 프로젝트가 완료되고 런칭되어서 데이터가 쌓이기전에 변경작업을 진행하자.
    ! Django application 을 시작하는 처음부터 user model을 교체하자. 무조건 교체하자. 교체할게 하나도 없더라도 inherit만 구현해놓자 !

#### [1_python]

    vscode내에서 python코드 및 django코드에 노란줄이 그어지며 인식은 하지못한다면 확장프로그램에 pylance를 설치해준다.
    pylance는 vscode를 위한 python 서버이다. 자동완성 및 import를 도와준다.
    Django가 shell내에 설치되어 vscode에서 인식이 되지 않는다.
    vscode하단 Select Language Mode에 python을 클릭하면 Select Interpreter 창이 열리며 사용할 Python 환경을 선택해주면된다. 오른쪽 text에 poetry가 있디면 그걸 선택해주면 된다.

    fomatter black을 설치해준다. 확장프로그램 설치로 적용이 되지 않는다면 인터넷에 검색하여 적용하자.
        정 안되면 노마드코더의 #5.0 Introduction 영상이나 댓글 및 Issues를 확인하자.

#### [2_Django]

    Users 앱을 생성 프로세스 진행힌다(startapp -> settings설치 -> migrate). migration은 오류확인을 위해 나중에 진행한다.
    해당 앱은 Django의 User를 상속받는다.
        from django.contrib.auth.models import AbstractUser

    프로젝트 시스템에 Django의 User를 상속받아 구현하여 사용할 것을 알려줘야한다. config>settings.py에 설정값을 넣어준다. 상단 User Document에 내용이 있다.
        #AUTH
        AUTH_USER_MODEL = "[myapp='users'].[MyUser='User']"

    migration시 오류가 발생한다.
        >>> Migration admin.0001_initial is applied before its dependency users.0001_initial on database 'default'.
    기존에 Django User에 생성된 user가 있어서 Django User를 상속받은 user app을 구현할 수가 없다.
    ! 기존의 db를 삭제 후 다시 migrate를 진행해야한다. db를 삭제하며 migrations폴더 내의 파일중 00XX_XXXX.py파일도 삭제한다. 그외 파일은 삭제하지 않는다.
    전체 migration을 다시 진행한다.

    user admin페이지 구현도 Django userAdmin을 상속받아서 하면된다.
        from django.contrib.auth.admin import UserAdmin

    User model을 커스텀한다. 기존에 Django Useradmin에 first_name과 last_name을 수정불가하도록 커스텀하였다.
        editable,
    컬럼을 추가한 후 makemigrations를 진행하면 오류가 발생한다.
        It is impossible to add a non-nullable field 'is_host' to user without specifying a default. This is because the database needs something to populate existing rows.
        Please select a fix:
        1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
        2) Quit and manually define a default value in models.py.
        Select an option:
    기존에 있는 유저에게 추가된 컬럼에 넣어줄 값이 정해져 있지 않아서 발생한 오류이다.
    default값을 정의해주든가 null값을 허용하면 된다. default값을 정의해준다.
    migration을 진행한다.

    User admin페이지에서 User정보 입력페이지에 들어가면 오류가 발생한다.
        'first_name' cannot be specified for User model form as it is a non-editable field. Check fields/fieldsets/exclude attributes of class CustomUserAdmin.
    User model에서 first_name과 last_name을 수정 불가하도록 적용했으나 Django Useradmin페이지에서는 수정하도록 설정되어 있어서 오류가 발생하였다.
    UserAdmin을 상속받은 클래스를 커스텀한다.
        fieldsets: model의 field가 보이는 순서를 설정. 일종의 섹션안에 field를 넣어서 그 섹션에 제목을 붙일 수 있다. 리스트나 튜플로 구성되어야한다.
        fields: model의 field가 보이는 순서를 설정.
        users>admin.py 참조
        UserAdmin의 permission과 Important dates을 복사해와 CustomUserAdmin>fieldsets에 붙여넣기하자.
        더보기.

<https://docs.djangoproject.com/en/4.1/ref/contrib/admin/#modeladmin-options>

    유저 커스텀이 완료되면 room model에서 user Foreignkey를 등록한다. on_delete는 필수값으로 설정한다.
        on_delete = models.SET_NULL: 외래키가 삭제되면 연결되어있는 컬럼은 Null로 적용된다.
                    = models.CASCAGE: 외래키가 삭제되면 연결되어있는 데이터도 같이 삭제된다.
    Foreignkey을 받은 컬럼은 Foreignkey의 ID값을 갖는다.
    추후에 ORM을 사용하여 데이터를 갖고오는 작업을 할 것이다. 매우 간단하게 구현할 수 있다.

    db.sqlite3를 시각화 하기위해서는 sqlite viewer 확장프로그램을 설치하면 된다.

## 6. Models and Admin

#### [2_Django]

    user model에 imagefield를 추가하면 서버에서 에러가 발생한다. pillow 프로그램이 있어야 ImageField를 사용할 수 있다.
    pillow를 설치한다.
    $ poetry add pillow

    db에는 text값을 넣어주면서 선택지를 고르는 field를 구현할 수 있다.
        class GenderChoices(models.TextChoices):
            {
                "[VALUE]": ("[actual value]", "[human readable name]"),
                ...,
            }

        gender = models.CharField(
            choice=GenderChoices.choices,
        )
    더보기.

<https://docs.djangoproject.com/en/4.1/ref/models/fields/#choices>

    rooms app을 설치한다.(startapp -> settings설치)
    model,admin 구현 후 migrate 하기로 한다.

    country와 city를 위한 package가 있다. 추후에 적용할 예정이다. TextChoices ?

    Room 모델을 구현후 amenity도 구현한다. rooms와 amenity는 many-to-many 관계를 갖는다.
    many-to-many는 room에서 여러 Amenity를 등록할 수 있다. many-to-many는  Foriegn과 다르게 on_delete값이 필수가 아니다.

    만들어진 날짜와 수정된 날짜를 추가해준다.
        created = models.DateTimeField(auto_now_add=True)

<https://docs.djangoproject.com/en/4.1/ref/models/fields/#datetimefield>

    생성된 날짜와 수정된 날짜는 많은 app에서 사용될 것이다. 모두가 사용가능한 공통코드를 담을 common app을 생성하자.
    common app을 생성 및 설치한다. common model은 데이터베이스에 추가하지 않을 model이다. 다른 model에서 재사용한다.
    common model은 abstract model로 만든다. abstract로 생성하면 django가 데이터베이스에 해당 앱 데이터를 생성하지 않는다.
    common은 절대 데이터베이스를 만들지 않는다. common model class에 추가해준다.
        class Meta:
            abstract = True
    그리고 commonModel을 사용할 model은 commonModel을 inherit 한다.

    Amenity 리스트에 표시되는 app이름이 Amenitys로 표기된다. Amenities 로 변경해준다.
        class Meta:
            verbose_name_plural = "Amenities"

    컬럼 추가 및 수정 창(add,change)에서 bold로 표시된 컬럼은 필수값이다.
    DateTimeField 컬럼을 filter에 추가하면 filter에 등록되어있는 값으로 filter하는 것이 아닌 현재날짜 기준으로 filter를 한다. (이번주, 이번해)
    수정불가한 데이터를 add-change창에서 확인할 수 있다.


    experiences app을 생성 및 설치한다.
    experience model과 experience model에서 사용할 perks model을 구현한다. 역시 many-to-many

    django는 add-change하는 도중에 foriegn컬럼을 추가할 수 있다.


    categories app을 생성 및 설치한다. category는 room과 experience에서 사용할 것이다.
    model 구현 후 room과 Experience에 추가해준다. migrate진행.

#### [1_python]

    문자열 메서드 title()을 사용하면 앞글자를 대문자로 표기해준다.

<https://zetawiki.com/wiki/%ED%8C%8C%EC%9D%B4%EC%8D%AC_title()>

    category __str__ return 부분에 kind 명을 대문자로 title()로 적용했다.

#### [2_Django]

    외래키를 사용하여 filter를 할 수 있다.


    review app 생성 및 설치를 한다.
    최대값을 설정할 수 있다.
        from django.core.validators import MaxValueValidator

        rating = models.PositiveIntegerField(
            validators=[MaxValueValidator(5)],
        )
    migrate 진행


    wishlists app 생성 및 설치.
    wishlist는 admin에서 생성을 진행하지 않기때문에 blank=True는 제외했다.
    migrate 진행


    bookings app 생성 및 설치. migrate 진행


    medias app 생성 및 설치. model> Photo, Video 구현.

    Direct Messages app 생성 및 설치. model> ChattingRoom, Message 구현
    apps.py>config 에 verbose_name 추가
        verbose_name = "Direct Messages"

    model, admin 구현은 마무리되었다.

## 7 ORM

#### [2_Django]

    ORM = Object Relationship Mapping. SQL 문을 사용하지 않고 엔티티를 객체로 표현할 수 있다. objects 는 데이터베이스 관리자이다.
    # ORM 의 정의

<https://hanamon.kr/orm%EC%9D%B4%EB%9E%80-nodejs-lib-sequelize-%EC%86%8C%EA%B0%9C/>

    # Django making Query

<https://docs.djangoproject.com/en/4.1/topics/db/queries/>
데이터 모델을 생성한 후 데이터베이스에 코드로 어떻게 접근할지 확인해보자.

    console로 명령어를 사용하요 확인할 수 있다. django>settings와 함께 python을 실행한다. shell 외에 python을 실행하면 Django를 포함하지 않는다.
    $ python manage.py shell

    model을 갖고 있기때문에 python에서 가져올 수 있다.
    >>> from rooms.models import Room

    django가 model을 생성할때 기본 제공하는 database objects가 있으며 여러 method를 갖고 있다.
        all()
        get([key]="[value]") # get()은 복수의 값을 가져올 수 없습니다. 복수의 값은 filter()를 사용
        save()

        >>> Room.objects.get(pk=1).amenities.all().get(name="Wi-Fi").description

        >>> r1 = Room.objects.get(pk=1)
        >>> r1
        <Room: beautiful Tent>
        >>> amenities = r1.amenities.all()
        >>> amenities
        <QuerySet [<Amenity: Wi-Fi>, <Amenity: swimming pool>]>
        >>> amenities.get(name="Wi-Fi").description
        '무선 인터넷'

#### [1_python]

    변수 정의 및 대입 한 다음 Django save()로 저장 가능.

#### [2_Django]

    obects는 Manager라 불린다. Manager는 데이터베이스와 소통할 수 있는 Interface 이다.
    # ORM 이란 무엇인가

<https://docs.djangoproject.com/en/4.1/topics/db/managers/>
model을 생성하면 Manager도 같이 생성된다. Manager도 수정적용 가능하다.

    여러객체 조회하기
        >>> for a in Room.objects.get(pk=1).amenities.all():
        ...     print(a.name)
        ...
        Wi-Fi
        swimming pool

    ? get()으로 가져오는 QuerySet에서는 var값으로 다시 가져올 수 가 있다.
        >>> Room.objects.get(pk=1).name
    하지만 filter()로 가져오면 오류가 발생한다.
        >>> Room.objects.filter(pk=1).name
        Traceback (most recent call last):
            File "<console>", line 1, in <module>
        AttributeError: 'QuerySet' object has no attribute 'name'
    get은 데이터 하나를 갖고 오지만 filter는 queryset으로 묶음으로 가져온다. get은 데이터가 없다면 오류가 발생하지만 filter는 빈 querySet을 반환한다.


    filter를 사용할 때 조건을 붙일 수 있다. field에 언더바 두개를 사용하여 조건값을 붙이거나 외부 모델 필드를 사용한다. lookup 이라 한다.
        >>> Room.objects.filter(price__gte=15)  # 15보다 크거나 같은 값
        # lookup 종류

<https://velog.io/@may_soouu/Django-%EB%A9%94%EC%86%8C%EB%93%9C-%EC%A0%95%EB%A6%AC>
<https://docs.djangoproject.com/en/4.1/ref/models/querysets/#field-lookups>

    console에서 데이터를 생성 및 대입하여 저장이 가능하며 삭제도 가능하다.
        create(): 데이터가 없는 빈 데이터 row가 생성된다.
        create([key]="[value]"): 데이터를 넣어주면서 row를 생성한다.
        get(...).delete(): 해당 데이터 삭제한다.

    QuerySet은 매우 게을러서 요청한 값만 전달해 준다. 내부에 어떤 값이 있는지 알지 못한다.
        get(...) -> <Room: beautiful Tent> # 이런식으로 <[model명]: [__str__]> 가져와서 전달한다.
    query에 select from ... 로 데이터를 다 긁어와서 한세월 걸리는 일을 방지해준다.

    Room admin에서 Room마다 amenities를 몇개 갖고 있는지 표시한다.
        1. amenities 를 계산한는 methon 를 model 에 추가한다.
        2. admin에 method를 넣어준다. admin method에 두번째 매개변수에 model 값을 보내준다.
    amenities 는 rooms 과 manyToMany관계이다. 그럼으로 querySet으로 데이터를 받아온다. filter().exclude().count() 사용가능하다.
        room.amenities.count()

    foriegn key를 역순으로 접근이 가능하다. 역순으로 접근을 filter를 사용할 때 lookup 과 컬럼명을 붙여서 사용가능하다.
        Room.objects.filter(owner__username='admin')
        Room.objects.filter(owner__username__startswith='ad')

    dir() 을 사용하여 속성들을 확인하자
        >>> dir(r1)
        ['DoesNotExist', 'Meta', 'MultipleObjectsReturned', 'RoomKindChoice', '__class__', '__delattr__',
        '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__',
        '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__',
        '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__',
        '__str__', '__subclasshook__', '__weakref__', '_check_column_name_clashes', '_check_constraints',
        '_check_default_pk', '_check_field_name_clashes', '_check_fields', '_check_id_field',
        '_check_index_together', '_check_indexes', '_check_local_fields', '_check_long_column_names',
        '_check_m2m_through_same_relationship', '_check_managers', '_check_model',
        '_check_model_name_db_lookup_clashes', '_check_ordering',
        '_check_property_name_related_field_accessor_clashes', '_check_single_primary_key', '_check_swappable',
        '_check_unique_together', '_do_insert', '_do_update', '_get_FIELD_display', '_get_expr_references',
        '_get_field_value_map', '_get_next_or_previous_by_FIELD', '_get_next_or_previous_in_order',
        '_get_pk_val', '_get_unique_checks', '_meta', '_perform_date_checks', '_perform_unique_checks',
        '_prepare_related_fields_for_save', '_save_parents', '_save_table', '_set_pk_val', '_state', 'address',
        'amenities', 'booking_set', 'category', 'category_id', 'check', 'city', 'clean', 'clean_fields',
        'country', 'created_at', 'date_error_message', 'delete', 'description', 'from_db', 'full_clean',
        'get_constraints', 'get_deferred_fields', 'get_kind_display', 'get_next_by_created_at',
        'get_next_by_updated_at', 'get_previous_by_created_at', 'get_previous_by_updated_at', 'id', 'kind',
        'name', 'objects', 'owner', 'owner_id', 'pet_friendly', 'photo_set', 'pk', 'prepare_database_save',
        'price', 'refresh_from_db', 'review_set', 'rooms', 'save', 'save_base', 'serializable_value', 'toilets',
        'total_amenities', 'unique_error_message', 'updated_at', 'validate_constraints', 'validate_unique',
        'wishlist_set']
    목록에 속성중 ..._set 항목이 역참조(reverse accesser) model이다. booking_set. Booking 모델에서 Room 모델을 참조한 것이다.
    모델명을 소문자로 가져온다음 _set을 붙여 생성한다.

    model 에 foriegn 지정한 칼럼에 related_name 값을 지정하여 _set 이름을 변경 할 수 있다. foreignKey, ManyToManyField 다 변경가능.
        related_name="rooms"
    [...]_set >>> [...]s 로 변경하였다.

## 8. Power Admin

#### [2_Django]

    Admin 페이지에서 데이터관리에 편리할 기능들을 더 추가할 것이다.

    방 리뷰 별점 평균 값을 계산하는 함수를 room model에 구현. 역참조 reviews를 호출하여 계산한다.
        def rating(self)
            ...
            else
                for review in self.reviews.all():
                    total_rating += review.rating
            ...
    해당 방식으로 ORM 을 작성하면 모든 컬럼을 불러와서 계산을 한다. rating 값만 가져오도록 최적화를 한다.
        values(): 해당 컬럼값을 가져옴
        for review in self.reviews.all().values("rating"):
            print(review)

        - 출력 값 -
        {'rating': 2}
        {'rating': 5}
        {'rating': 4}
        {'rating': 5}
    {'컬럼명': value} 형식의 딕셔너리로 값을 가져온다. review.rating 부분을 수정해야 한다.

#### [1_python]

    dictionary 에 value값을 가져오는 식
        review["rating"]
    value 불러오는 부분을 수정해준다.

#### [2_Django]

    검색창 기능을 room models에 구현한다. 기본 검색 컬럼은 검색어가 포함된 값들을 불러온다.(=__contains). price는 정확한 값으로 검색하도록 적용.
        "price__exact",
    __exact 대신에 컬럼앞에 =를 붙이는 것과 같은 의미를 갖는다.
        "price__exact" == "=price"
    # search field

<https://docs.djangoproject.com/en/4.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields>

    foriegnKey 값을 검색할 수 있다. LookUp에 ForiegnKey 의 컬럼을 넣을 수 있다.
        "owner__username",

    admin 화면에 action창의 기능을 추가한다. admins.py 에 @admin.action 을 추가한 다음 admin내 actions을 추가해준다.
        @admin.action(descriptions="...")  # descriptions: action 창에 표기될 text
        def reset_price(model_admin, request, queryset):
            ...

        class RoomAdmin(admin.ModelAdmin):
            actions = (reset_price,)

    request 와 dir(request) 값
        request: <WSGIRequest: POST '/admin/rooms/room/?q=gh'>  # gh은 내 id 이다.
        dir(request): ... 여러 method 와 컬럼. user컬럼이 있으며 해당 action을 실행한 user의 데이터가 있다.
    user의 권한에 따라 해당 action 이 실행이 안되도록 막을 수 있다.

    for문을 이용하여 reset_price 기능을 구현한다.
        for room in rooms.all():
            room.price = 0
            room.save()

    reviews 필터를 추가 구현한다. foreignKey 를 사용하여 필터를 추가한다.
        "user__is_host",
    foreignKey의 foreignKey를 가져올 수 있다. foreignKey의 foreignKey의 foreignKey의 ...
        "room__category",

    Django 에는 필터 구현을 위한 클래스가 있다. 하지만 필터 구현을 위한 기본 기능은 충분하다.
    특정 payload 값이 포함된 컬럼을 필터하는 클래스를 구현해본다.
        class WordFilter(admin.simpleListFilter):
            title= "..."
            parameter_name = "..."
            def lookups():

            def queryset():

        # simpleListFilter

<https://docs.djangoproject.com/en/4.1/ref/contrib/admin/filters/#using-a-simplelistfilter>

    title, parameter_name, lookups(), queryset() 를 필수로 구현해야한다.

    parameter_name 은 url에 표기될 key일 뿐 데이터를 가져오는데는 관여하지 않는 것 같다.

    딕셔너리 형식 데이터를 Python에서 데이터가져오는 방식이 아닌 Django에서 가능한 방식이 있다.
        self.value() == self["key-name"]

    !코드 챌린지. review rating 값이 3미만과 3이상의 값을 분류하는 filter를 만들어보자.

## 9. urls and views

#### [2_Django]

    config>urls 에는 사용자가 특정 url에 접근을 하면 해야할 행동들이 적혀 있다.
    urls 파일에 모든 url을 다 적을 수 있지만 어플리케이션마다 urls 파일을 생성하여 분리한다.

    그 url을 실행할때 할 행동을 views파일에 구현 한다.
    views.py 파일명은 어떤거여도 상관없다.  import하여 사용할 것이다.

    views 에 hello world를 구현해본다.
    - views.py -
        from Django.http.response import HttpResponse

        def say_hello(request):
            return HttpResponse("Hello world!")

    - config>urls.py -
        import bookings import views as booking_views

        urlpatterns = [
            ...
            path("bookings/", booking_views.say_hello)
        ]
    HttpResponse로 데이터를 보내준다. 브라우져 url ./bookings 에서 텍스트 데이터를 확인할 수 있다.

    model 마다 urls.py파일을 생성하여 urls를 추가한다.
    그리고 config>urls 에는 include를 사용하여 config>urls에 등록한 url 을 포함한 url에 접근을 하면 include("[file path]") 로 이동한다.
        path("rooms/", include("rooms.urls")),  # rooms/뒤에 뭐가 붙든 rooms.urls로 이동한다.
    rooms.urls 에는 urlpattern을 구현한다.
        urlpatterns = [
            path("", views.say_hello)
        ]
    rooms>urls에는 홈 path는 ./rooms/ 이다. 그렇기때문에 path()에 ./rooms/ url에 해당하는 값은 ""(null)값을 넣어주면 된다

    path() url에 변수값을 받을 수 있다. 변수 타입과 변수명을 넣어주면 된다.
    - urls -
        path("<int:room_id>", views.see_ane_room)

    - views -
        def see_one_room(request, room_id):
            ...
    변수값을 함수에 인수로 준다. Django에서 변수 타입을 체크해준다. path내 변수명과 함수 매개변수명이 일치해야하며 순서는 상관없다. request 뒤에만 위치하면 된다.

    ! 이번 프로젝트에서는 사용하지 않는다.
    render를 이용한 temlates를 불러오게 구현한다. Django의 render를 사용하며 기본으로 import 되어있다.
    - views -
        from .models import Room

        def see_all_rooms(request):
            rooms = Room.objects.all()
            return render(
                request,
                "all_rooms.html",
                {
                    "rooms": rooms,
                    "title": "Hello! This is Title~",
                },
            )
    render()는 template_name 을 templates 폴더내에서 파일을 불러온다. templates 폴더와 all_room.html 파일을 생성한다.
    - templates>all_rooms.html -
        <h1>{{title}}</h1>  # {{"변수명"}}. django에서 데이터를 바인딩해준다. python 웹스크립퍼만들기 강의에서 기초 이론을 알려준다.
        <span>{{rooms}}</span>  # 해당 방식으로 하며 queryset으로 표현이 된다.
    rooms list 구현이다. 앵커를 이용한 각 방페이지로 이동까지 구현했다.
        <ul>
            {% for room in rooms %}
            <li>
                <a href="/rooms/{{room.pk}}">
                    {{room.name}}<br />
                    {% for amenity in room.amenities.all %}
                        <spna>-{{amenity.name}}<br /></span>
                    {% endfor %}</a
                >
            </li>
            {% endfor %}
        </ul>

    request 데이터를 받을때 해당 페이지가 없을 경우 보여줄 페이지를 구현한다.
    DoesNotExist 는 Model 안에 있다. try-expect문을 사용한다. not_found는 임의의 데이터다.
    - views -
        try:
            ...
        except Room.DoesNotExist:
            return render(
                request,
                "room_detail.html",
                {
                    "not_found": True,
                },
            )
    - room.detail.html -
        {% if not not_found %}
            <h3>Room id: {{room.pk}}</h3>
        {% else %}
            <h3>404 not found</h3>
        {% endif %}

    이번 프로젝트는 프론트엔드를 react로 구현할 것이기 때문에 view에서 templates를 호출하는 상단 코드 방식은 사용하지 않을 것이다.
    template만으로 다이나믹한 페이지를 표현하지 못한다. 하지만 대체로 많은 프로젝트는 장고의 템플릿 기능만 사용해도 가능하다.
    추후에 템플릿 만으로 프로젝트를 완성해보자.
    # templates

<https://docs.djangoproject.com/en/4.1/topics/templates/>

## 10. Django Rest Framework

#### [5_Rest]

    장고 Rest 프레임워크는 장고로 API를 아주 쉽게 만들 수 있는 패키지이다. 많은 shortcut를 제공해준다.
    회사에서 장고를 사용한다면 Rest프레임워크를 사용할 것이다. 산업표준으로 될정도로 전부 rest framework를 사용한다.
    Django서버에서 json파일을 react UI에게 보내준다. 실제로 URL로 직접 이동하지 않는다. 그저 데이터를 전달해준다.
        react는 사용자에게 url을 받아서 데이터를 요구하면 Django App은 해당 데이터를 찾아주며 react는 url로 이동하며 화면을 표현한다.

    우선 Rest framework 를 설치한다.

<https://www.django-rest-framework.org/#installation>

    poetry를 사용하기 때문에 pip대신에 poetry 명령어로 설치한다. pip i -> poetry add
    $ poetry add djangorestframework
    config>settings 에 추가해 주자. THIRD_PARTY_APPS[] 를 추가해서 앱을 설치한다. INSTALL_APPS 에 THIRD_PARTY_APPS 를 추가한다.

#### [2_Django]

    categoris>urls 파일을 생성하고 url에서 view를 호출하는 기본 코드를 작성한다.
    view를 작성한다. 기존 템블릿을 사용하지 않고 json을 보내준다. django의 JsonResponse 를 사용해보자.
        from django.http import JsonResponse

        def categories(request):
            categories = Category.objects.all()
            return JsonResponse(
                {
                    "ok": True,
                    "data": categories,  # 해당 데이터를 읽을 때 오류가 발생한다.
                }
            )
    queryset을 JsonResponse()로 보내게 되면 형식오류로 에러가 발생한다. 브라우져는 querySet을 읽을 수 없다. querySet을 JSon으로 변형해야 한다.

    Django의 serializer을 사용해보자.
    # Django의 serializer 대신에 rest_framework의 serializer를 사용한다. 참고용으로만 보자.

<https://docs.djangoproject.com/en/4.1/topics/serialization/#djangojsonencoder>

        from django.core import serializers

        ...
            return JsonResponse(
                ...
                "data": serializers.serialize("json", categories),
            )

#### [5_Rest]

    Django는 serializer는 매법 데이터를 보낼때마다 데이터변형이 필요하며 전송데이터 조작이 복잡하다.
    Django의 serializer를 대신헤 rest_framework의 serializer를 사용한다.
    # rest_framework의 request, response

<https://www.django-rest-framework.org/tutorial/2-requests-and-responses/>

        from rest_framework.decorators import api_view
        from rest_framework.pagination import Response

        @api_view()  # 관리자가 데이터를 확인 및 수정할 수 있는 view를 생성해준다.
        def categories(request):

            return Response(
                "ok": True
            )
    이전 운명하신 프로젝트에서 계속 봐오던 아름다운 JSon페이지가 나왔다. api화면과 json화면 중 골라서 볼 수 있다.
    model명, CRUD호출, 통신 상태 등 데이터를 확인 할 수 있다.

    데이터 변형을 하기위해 model내에 serializers.py를 생성한다. 앞으로 데이터를 변형할때 규칙을 정의 할 것이다.
    - serializers -
        from rest_framework import serializers

        class CategorySerializer(serializers.Serializer):
            name = serializers.CharField(required=True)  # model의 데이터타입을 알려준다. 변수명은 model명과 일치해야한다.
    데이터 변형하여 보내준다.
    - views -
        from .serializers import CategorySerializer

        categories = Categories.objects.all()
        serializer = CategorySerializer(categories)
        return Response(
            "data": serializer.data
        )
    >>> AttributeError at /categories/
        Got AttributeError when attempting to get a value for field `name` on serializer `CategorySerializer`.
        The serializer field might be named incorrectly and not match any attribute or key on the `QuerySet` instance.
        Original exception text was: 'QuerySet' object has no attribute 'name'.
    오류 발생...
    여러 데이터(리스트)를 보낼때는 many 옵션을 부여해야한다.
        serializer = CategorySerializer(categories, many=True)

#### [2_Django]

    하나의 객체를 볼 화면을 구현해본다. url에 변수를 받고 view 에 구현할 클래스에 변수를 인수로 받아 사용하면 된다. get()사용
    - views -
        def category(request, pk)  # 인수는 urls에 사용된 변수명을 그대로 사용해야한다.
            category = Category.objects.get(pk=pk)
            ...

#### [5_Rest]

    @api_view() 의 기본 설정은 get방식만 받는다. 매개변수에 리스트형식으로 값을 넣어줘서 형식을 추가할 수 있다.
        @api_view(["GET", "POST"])
    api_view() 는 POST형식을 추가하면 브라우져에서 post테스트 바로 해볼 수 있는 prompt을 지원한다.
    프로토콜 방식에 따라 다른 로직이 타도록 적용한다.
        if request.method == "GET":
            ...
        elif request.method == "POST":
            ...
    request 값을 통해 data를 넣어 줄 수 있다.
        ...
        Category.objects.create(
            name = request.data["name"],
            kind = request.data["kind"],
        )
    하지만 이렇게 데이터를 넣어주면 데이터 검증없이 바로 생성이된다. 이 방식은 사용하지 않는다.
    Serializer를 사용하면 브라우져에서 오는 json파일을 queryset으로도 변경해준다. serializer설정을 그대로 사용하면 된다.
    serializer에서 데이터 유효성검사를 한다. model에 있는 설정을 serializer에 그대로 사용해주면 된다.
    json형식을 변형할때는 serializer() 안에 값을 그냥 넣어주지 않으며 data값을 지정해주며 넣어줘야한다.
        serializer = CategorySerializer(data=request.data)

    querySet으로 변경한 데이터 유효성을 확인할 수 있다.
        print(serializer.is_valid())  # True, False 체크
        print(serializer.errors)  # 에러를 표시해준다.
    위방식을 이용하여 데이터 유효성검사를 하여 에러메세지를 표기할 수 있다.
        if serializer.is_valid():
            ...
        else:
            return Response(serializer.errors)
    pk, created_at 값을 제외한 데이터를 넣어주니 pk와 created_at값을 보내주지 않았다며 알려준다.
    해당값에 read_only옵션을 부여하면된다. model 정의를 따라 값을 넣어준다. (pk = 키넘버, created_at = 지금 시간)
        pk = serializer.IntegerField(read_only=True,)

    model 에서 사용하던 charField의 choices 가져와 사용할 수 있다.
    다만 serializer 에서는 charField 대신에 choiceField 를 사용해야 한다. choiceField 는 max_length 를 사용하지 않는다.

    serializer 에 save()가 있다. request.data 만을 받아 serializer.save()를 호출하면 serializer내의 create()를 호출한다.
    create() 두번째 인수로 validate data 를 받으며 객체를 return해야 한다.

#### [1_python]

    여러 인수를 받을 때 변명앞에 *를 붙이면 여러 변수를 받을 수 있다. 다수의 딕셔너리를 받을때는 **를 붙여서 사용하면 된다.
        **validated_data

#### [2_Django, 5_Rest]

    serializer>create() 함수에 return 을 구현 해준다.
        create(self, validated_data)  # 해당 create()는 serializer의 create 이다.
            return Category.objects.create(**validated_data)  # 해당 create()는 objects의 query create 이다.

#### [6_JSon]

    변수명을 담을 때는 큰따옴표를 사용해야한다. (작은 따옴표 X)

#### [5_Rest]

    PUT신호를 받을 때 업데이트가 실행되도록 코드를 구현해보자. POST신호로 모든걸 실행하도록 적용 할 수도 있지만 분리 구현하도록 하겠다.
    전체페이지가 아닌 각 객체 페이지에서 수정이 되도 적용한다.
        @api_view(["GET","PUT"])
    GET 부분을 먼저 구현한다. 전체객체 조회와 달리 없는 객체를 호출할때를 위헤 try-extact 를 사용하여 예외처리를 한다.
        from rest_framework.except import NotFound  # 팁이라면 notfound 소문자로 입력하면 자동완성으로 인식이 안된다.
        ...
            try:
                category = Category.objects.get(pk=pk)
            excapt Category.DoesNotExist:  # view함수 category가 아닌 model Category이다.
                raise NotFound  # raise 예외 처리에는 raise를 사용한다.

    ! serializer에는 python객체인 Django Model을 넣어주면 된다.
        serializer = CategorySerializer(data=request.data)
        update_data = serializer.save()
        print("serializer >>>:", type(serializer))
        print("update_data >>>:", type(update_data))
        serializer = CategorySerializer(update_data).data

        serializer >>>: <class 'categories.serializers.CategorySerializer'>
        update_data >>>: <class 'categories.models.Category'>  # >>> Rooms: 미치광이 방
    !

    Update 를 위해 serializer에 변경할 객체와 데이터를 같이 보내준다.
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(
            category,
            data=request.data,
            partial=True,  # 보내지 않는 일부 데이터는 기존 데이터로 저장한다. 필수값을 보내지 않아도 된다.
        )
        serializer.save()  # 이 save에서는 update()가 호출된다. serializer에 instance 인수를 보내면 update() overroading.

#### [1_python]

    ! 지역변수가 함수밖에서 사용이 가능하다. 왜?
        @api_view(["GET", "PUT"])
        def category(request, pk):

            print(category)  # 전역변수인지 확인차 사용해봄. 오류 발생. 전역변수는 아닌거 같다.
            try:
                category = Category.objects.get(pk=pk)
                print(category)
            extact:
                ...
            if ... :
                print(cateogry)  # 오류가 발생하지 않으며 사용이 가능. 뭐지???

#### [5_Rest]

    serializer>update()를 구현한다. 기본 python문법으로 표현하면
        def update(self, instance, validated_data):
            if validated_data["name"]:
                instance.name = validated_data['name']
            ...  # 각 객체마다 계속 if문을 넣어줘야한다. 코드가 길어진다.
    Dictionary에 있는 .get() 를 이용하여 리스트 객체를 넣어주자.
        instance.name = validated_data.get("name", instance.name)  # 두번째 인수는 찾는 값이 없을 경우 default 값이다.
        ...  # 이것도 각 객체마다 계속 추가해줘야한다.
        instance.save()  # save() 호출하지 않으면 오류발생. >>>: `update()` must be implemented.
        return instance

    각 객체 페이지 함수에 DELETE 를 구현해본다. api_view()에 delete를 추가해준다.
    추가 후 delete()를 구현한다.
        from rest_framework.status import HTTP_204_NO_CONTENT
        ...
            if request.method == "DELETE":
                category.delete()
                return Response(data=HTTP_204_NO_CONTENT)
    페이지에 delete버튼이 생성된다. 버튼을 클릭하며 재확인 창이 뜨며 rest_framework가 데이터를 한번더 보호해주며 확인 클릭시 삭제를 진행할 수 있디.


    지금까지 작성한 url은 admin한 페이지의 일부처럼 보일 수 있어서 변경을 진행한다. 확실히 API url 로 인지되도록 변경한다.
    config>url에 admin을 제외한 urls는 앞에 'api/<버젼>/' 을 붙인다.
        path("api/v2/categories/", include("categories.urls")),
        ...

    @api_view() 를 사용하여 함수를 구현하는 대신에 클래스를 사용하여 구현할 수 있다. categories()를 대신하여 Categories 클래스를 구현한다.
    # api 가이드

<https://www.django-rest-framework.org/api-guide/views/>

    - views -
        from rest_framework.views import APIView

        class Categories(APIView):

            def get(self, request):  # if문 대신에 함수를 사용해주면 된다.
                ...

            def post(self, request):  # 추가해준 함수명만 프로토콜 허용에 추가된다. (지금 구성에서는 Allow: GET, POST, HEAD, OPTIONS). 그러므로 함수명은 프로토콜명과 같게 사용한다.
                ...
    - urls -
        path("", views.Categories.as_view())  # as_view() 를 호출해야 프로토콜마다 get,post 함수를 실행시켜 준다.

    CategoryDetail 클래스(<- category() )도 위와 같이 구현을 한다. category()에는 pk값을 갖는 category를 찾는 중복된 코드가 존재한다.
    rest framework의 관습(convention)을 사용하여 중복되는 코드를 실행하는 함수를 구현한다.
    # detail views 구성

<https://www.django-rest-framework.org/tutorial/3-class-based-views/>

        def get_object(self, pk):
            ...
            return category

        get, put, delete(self, request, pk):
            category -> self.get_object(pk) 변경
    한개의 객체를 가져올때(Detail) pk를 사용하여 값을 가져올때 사용된다.

    model의 기본 모형을 갖고 serializer를 생성할 수 있다.
        class CategorySerializer(serializers.ModelSerializer):  # Serializer -> ModelSerializer
    클래스를 Meta 클래스를 이용하여 정의한다.
        class Meta:
            model = Category
            fields = "__all__"  # fields <> exclude
    이 세줄로 기존 serializer의 구현을 대체할 수 있다. create() 와 update()도 생성해준다.

    rest framework 의 viewset을 가져와서 views를 쉽게 구성할 수 있다.
    # viewsets 구성 및 urls 구성방법

<https://www.django-rest-framework.org/api-guide/viewsets/>

        from rest_framework.viewsets import ModelViewSet

        class CategoryViewSet(ModelViewSet):

            serializer_class = CategorySerializer  # 이 두가지는 필수로 적용해줘야한다.
            queryset = Category.objects.all()
    urls에 as_view()에 사용할 프로토콜을 추가해줘야 한다.
        path("", "views.CategoryViewSet.as_view({
            "get": "list",
            "post": "create",
        }))
    detail 페이지를 위한 path 도 구성해준다.
        path("<int:pk>", "views.CategoryViewSet.as_view({
            "get: "retieve",  # pk를 이용한 detail search
            "put": "partial_update",
            "delete": "destroy",  # 세 프로토콜은 pk값을 받는다.
        }))

    viewset 은 웹페이지에 기본 데이터 변경 구성을 갖는 Row data 탭과 html form 탭을 제공해준다.

    더많은 rest framework의 마법적이 기능들을 확인하고 싶다면 tutorial을 더 활용해보자.

<https://www.django-rest-framework.org/tutorial/quickstart/>

    viewset을 사용하게 되면 자동으로 완성되는 부분이 많아져서 코드가 단축되지만 코드가 너무 추상적으로 변한다.
    그리고 추가기능을 구현할 때 코드가 더 길어지게 되는 경우가 발샐할 수 있다. 그때에는 전체를 다시 구현을 할지 viewset에서 커스텀할지 결정해야한다.
    대체로 apiview를 다시 작성하는 것이 더 편리하며 관리상에도 좋다.

## 11. Rest API

#### [5_Rest]

    API 생성을 시작한다. 보안에는 신경쓰지않으며 우선 기능 구현초점으로 진행한다.

    rooms>Amenity 구조를 구현한다. ModelSerializer 를 사용하면 model에 적용되어있는 read only도 같이 적용된다.
    views 는 APIView를 참조했다.

    같은 구조로 experiences>Perk를 구현했다.

    앞서 만든 api는 기존에 [10. Django Rest Framework]에서 배웠던 방식을 사용하여 복습하는 겸 만들어 봤다.
    이제 Rooms model부터 구조를 다 만들어본다. Authentication 과 relationship 을 새로 배워서 사용해본다.
    room serializer도 ModelSerializer를 사용하며 view 데이터를 json으로 변형한다.

    값을 일부만 가져오는 RoomListSerializer를 만든다.

    개별 객체를 가져오는 RoomDetail api를 생성한다. (url: <int:pk>, view, serializer)
    foriegn키를 가져오는 컬럼은 데이터를 표시할때 pk값을 표시한다.
    foriegn키 값을 확장해서 전체값을 가져올 수 있다.
    - serializer_Meta -
        depth = 1
    foriegn키의 값을 전부 전달해 준다. 데이터가 가져오는 양이 많아져 매우 느려지게 되며 사용자의 개인정보까지 보내져 보안에 문제가 발생한다.
    RoomDetail에 표기할 user의 데이터만 가져올 serializer를 생성한다.
    - users>serializers -
        class TinyUserSerializer
    rooms>serializers 에 depth=1 대신에 foriegn키 컬럼마다 serializer를 지정해주면 된다.
        owner = TinyUserSerializer()  # Meta 클래스 안이 아닌 serializer 클래스안에 작성해주면 된다.
        amenities = AmenitySerializer(many=True)  # 값이 여러개일경우 many를 활성화해준다.

        class Meta:
            ...  # depth는 삭제해 준다.


    room의 post 기능을 구현해본다. foriegn키를 제외한 컬럼에 값을 넣을때는 오류가 발생하지 않는다.
    하지만 foriegn키에 값을 넣을때는 입력오류가 발생한다.
    # 11.6 Room Owner

<https://nomadcoders.co/airbnb-clone/lectures/3909>

    owner는 사용자값을 request에서 받아서 입력하지 않는다. 사용자가 입력하는 유저값을 넣어서는 안된다. 우선 owner설정은 read_only를 넣어준다.
        owner = TinyUserSerializer(read_only=True)

    request objects 중에 request 를 보낸 사용자의 데이터를 갖고 있는것이 있다.
        request.user
    save() 에 컬럼 값을 기입할 수 있다.
        serializer.save(owner=request.user)  # >>> 'owner': <SimpleLazyObject: <User: G.H.Byeon>>

    request.user.is_authenticated 를 사용하면 사용자의 로그인여부를 알 수 있다. (로그인 일경우 = True)
        def post(self, request):
            if request.user.is_authemticated:
                ...
            else:
                raise NotAuthenticated
    post() 유효검사 후 로직 실행

    save()>create() 가 실행될때 room의 model값중 foriegn키를 제외한 값이 전송이 된다. foriegn키를 찾아서 넣어줘야 한다.
    category를 입력값을 받는지 확인 및 식별 후(식별? 단어가 생각이 안난다.) save()에 값을 넣어준다.
        category_pk = request.data.get("category")
        if not category_pk:
            raise ParseError
        try:
            category = Category.objects.get(pk=category_pk)
            if Category.CategoryKindChoice.EXPERIENCES:  # 카테고리가 경험일 경우 에러 발생.
                raise ParseError("The category kind should be 'rooms'.")
        except Category.DoesNotExist:
            raise ParseError("Category is not found.")  # 오류 내용을 보내줄 수 있다.
        ...
            created_room = serializer.save(
                owner=request.user,
                category=category,
            )

    ManyToManyField 값인 Amenities를 가져와 보겠다.
    Amenity 는 값을 보내지 않아도 에러를 발생하지 않도록 적용하겠다. room생성 후에도 나중에 항목들을 추가 가능하도록 적용한다.
        created_room = serializer.save(...)  # save() 다음에 구현한다
        amenities = request.data.get("amenity")
        try:
            for amenity_pk in amenities:
                amenity = Amenity.objects.get(pk=amenity_pk)
        except Amenity.DoesNotExist:
            raise ParseError(f"Amenity with id {amenity_pk} is not found.")
    ManyToManyFields 는 add(), remove() 를 사용하여 객체를 리스트에 추가, 제거를 하여 저장한다.
        created_room.amenities.add(amenity)  # pk가 아닌 객체를 넣어준다.

    유효성 검사에서 오류가 발생한다면 room을 삭제하여 재생성하도록 유도가 가능하다.
        except Amenity.DoesNotExist:
            created_room.delete()
    이번 프로젝트에서는 amenity가 잘못되어도 room은 생성되도록 하였기때문에 삭제는 구현하지 않았다.

#### [2_django]

    Django에서는 쿼리가 실행되면 DB에 바로 적용이 된다.
    하지만 transaction 을 사용하며, 많은 쿼리와 create()를 정의한 다음에 그중에 하나라도 실패하면 모든쿼리는 취소된다.

<https://docs.djangoproject.com/en/4.1/topics/db/transactions/>

    transaction.atomic(): 내에 코드는 전체 실행이 되고나서 한번에 데이터 변경이 이뤄진다.
        from django.db import transaction

        ...
            with transaction.atomic():
                created_room = serializer.save(...)
                ...  # 내부 try-except문은 삭제한다.
    try-except문을 사용하면 transaction은 에러가 난 사실을 알지 못한다.
    transaction문을 try-except문으로 감싸준다.

#### [5_Rest]

    room_delete() 구현한다. 로그인 접속여부와 삭제자와 룸생성장가 같은지 확인한다.
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if request.user != room.owner:
            raise PermissionDenied

    room_put() 도 로그인 접속 여부와 삭제자 식별을 진행한며 저장 데이터 검증을 진행한다.
    rooms_post와 달리 category_pk여부에 따라 category를 넣고 저장할지 그냥저장할지 정하며 Amenity저장하기 전에 clear해준다.
        if category_pk:
            room = serializer.save(category=category)
        else:
            room = serializer.save()

        ...
            room.amenities.clear()

    SerializerMethodField: 기존 model외의 값을 가져올 수 있다. 메서드 이름은 속성앞에 get_을 붙여야한다.
        potato = serializers.SerializerMethodField()

        get_potato(self, room):
            return ...

#### ! username of userModel's Serializer

    username = CharField(help_text='150자 이하 문자, 숫자 그리고 @/./+/-/_만 가능합니다.', label='사용자 이름', max_length=150, validators=[<django.contrib.auth.validators.UnicodeUsernameValidator object>, <UniqueValidator(queryset=User.objects.all())>])

#### [5_rest]

    context를 사용하여 외부에 데이터를 보낼때 유용하다. serializer 호출 인수에 context=() 를 추가해 주면 된다.
    - views -
        RoomListSerializer(... , context=("hello": "bye bye"), )
    - serializer -
        def get_...(self, room):
            print(self.context)
    user의 데이터를 가져와 serializer에 보내어 해당 room의 owner인지 대조하는 로직을 작성한다.
    - views -
        RoomListSerializer(... , context={"request": request}, )
    - serializer
        is_owner = serializers.SerializerMethodField()
        fields = (
            ...
            "is_owner",
        )
        def get_is_owner(self, room):
            return room.owner == self.context["request"]  # True or False

    GET과 PUT serializer가 분리되어 있지 않기 때문에 다른 프로토콜에서 에러가 발생할 수 있다. 확인 후 다른 프로토콜도 작업 진행.
    데이터를 변활할때는 오류가 발생하지 않지만 Response로 데이터를 보낼때 context값을 보내지 않는다면 오류가 발생한다.
        serializer = RoomDetailSerializer(
            data=request.data,   # It's OK
        )
        created_room = serializer.save(
            owner=request.user,
            category=category,
        )

        serializer = RoomDetailSerializer(
            created_room,
            context={"request": request},   # You should be response the context.
        )
        return Response(serializer.data)

    reviews 역참조자를 사용하여 roomDetail에서 불러온다.
    역참조를 사용하여 데이터를 가져올때 review data가 매우 많을 수 있다. 페이지가 위험해질 수 있다.

    데이터 양을 조절하기 위해서 pagination기능을 추가해야하며 1개의 room을 위한 review 전용 페이지를 생성한다.
    페이지를 url parameter로 가져오기로 한다. parameter은 request에 담긴다.
        url: http:// ... /reviews?page=4  # ?: query를 보내는 기호
        print(request.query_params)  # >>>: <QueryDict: {'page': ['4']}>
    페이지 param을 가져온다. 값이 없을 경우 default값을 가져올 수 있다.
        page = request.query_params.get("page", 1)  # get("page", 1): page값이 없을 경우 1을 return, 해당값은 string타입이다.
    url parameter값은 string type이기때문에 형변환 시켜줘야한다.
        page = int(page)
    페이지 값이 없거나 string값을 보내올 경우를 위해 try-except문을 사용한다.
        try:
            page = request.query_params.get("page", 1)
            page = int(page)
        except ValueError:
            page = 1

    page param값으로 pagination기능을 구현한다.
        page_size = 3
        start = (page - 1) * page_size
        end = start + page_size

        reviews = room.reviews.all()[start:end]  # .all()[offset:limit]: 리스트에서 뽑듯이 all() 객체에서도 인덱스 구역을 정해 값을 가져올 수 있다.

<https://docs.djangoproject.com/en/4.1/topics/db/queries/#limiting-querysets>

    pagination 기능을 이용하여 amenities 페이지도 구현.

    page_size 셋팅값을 config>settings에 설정을 하고 가져와서 사용하는 것으로 설정한다.
    - config>settings -
        PAGE_SIZE = 3
    - views -
        page_size = 3 -> settings.PAGE_SIZE


    파일 업로드 기능을 구현한다. Media>photo 파일을 upload하고 파일을 열면 Page not found Error가 발생한다.

<https://docs.djangoproject.com/en/4.1/howto/static-files/#serving-files-uploaded-by-a-user-during-development>

    장고에서 파일 업로드을 할경우 기본 root에 저장을 한다. config>setting에 업로드 path를 설정할 수 있다.
    - config>settings -
        MEDIA_ROOT = "upload"
    파일 업로드시 upload 폴더가 생성되며 폴더내에 파일이 생성된다.

    하지만 파일을 열경우 아직도 에러가 발생한다. 업로드된 파일을 열수 있는 url을 설정해 줘야한다.
    - config>settings -
        MEDIA_URL = "user-uploads/"  # MEDIA_URL setting must end with a slash
    파일을 열때 MEDIA_URL로 이동하여 파일을 찾는다. Django에게 user-uploads를 노출시켜달라고 말해야한다.
        from django.conf.urls.static import static
        from django.conf import settings  # settings.py에 대한 프록시(==from config import settings)

        urlpatterns = [
            ...
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    이제 파일이 정상적으로 열릴것이다. 하지만 이 구조는 서비스환경에서는 권장되지 않는다.
    신뢰하지 않는 유저에게 업로드되는 컨텐츠를 수락하는 경우에 위험해질 수 있다. 업로드 되는 파일들이 소스가 있는 피시에 다운로드가 직접되는 거다.

<https://docs.djangoproject.com/ko/4.1/ref/settings/#media-url>

    파일을 호스팅하는 서비스에 파일을 넣은 다음, 장고에겐 URL을 제공하기로 한다. (아마존이나 구글 클라우드를 쓰는것이 더 편하다.)
    Medias model클래스의 ImaageField, fileField 컬럼 속성을 변경한다.
        file = models.URLField()
    migration 진행 (오랜만이다.)

    RoomPhoto post()를 구현한다.
        사용자 인증
        보내온 데이터 검증 및 저장
        저장데이터 재전송


    APIView의 permissions 프로퍼티를 변경하여 유저 검증을 할 수 있다.
        from rest_framework.permissions import IsAuthenticated

        ...
            permission_classes = [IsAuthenticated]
    GET은 모든 사람이 호출 가능한 프로토콜이다. 권한이 필요없는 프로토콜이 포함되어 있다면 readonly도 같이 부여한다.
        from rest_framework.permissions import IsAuthenticatedOrReadOnly

        ...
            permission_classes = [IsAuthentucatedReadOnly]
    권한이 필요없느 GET만 있다면 권한이 없어도 된다.


    room>RoomReviews POST 작업 진행.


    wishlists 작업을 진행한다. wishlist는 사용자가 등록한 wishlist만을 본다. all() 대신에 filter()를 사용하며 권한도 자신만 가능하도록 한다.
        permission_classes = [IsAuthenticated]

        ...
            all_wishlists = Wishlist.objects.filter(user=request.user)
    GET, POST 작업 진행.


    wishlist 작업 진행. ("<int:pk>" ,WishlistDetail - GET,PUT,DELETE)
    wishlists와 같이 본인만 접근이 가능. 추가로 user를 같이 넣어주면서 본인 wishlist만 가져오도록 적용한다.

        def get_object(self, pk, user):
            ...
            return Wishlist.objects.get(pk=pk, user=user)

        def get(...):
    wishlistDetail 에서는 wishlist 명만 변경이 가능하도록 한다.

    wishlistToggle에서는 list를 변경하는 기능을 구현한다. room을 좋아하는 버튼을 클릭할때마다 변경이 되도록 적용할 것이다.
    room pk는 request 로 전달해도 되며 url로 전송도 가능하다. 둘 중 편한 방법으로 사용하면 되며 여기선 url로 받도록 적용한다.
        def get_list(self, pk, user):
            ...

        def get_room(self, pk):
            ...

        def put(self, request, pk, room_pk):
            wishlist = self.get_list(pk, request.user)
            room = self.get_room(room_pk)

            if wishlist.rooms.filter(pk=room.pk).exists():  # ManyToManyField 는 querySet으로 데이터를 가져오기때문에 all(),filter()가 사용가능하다.
                                                            ## exclude()는 데이터 존재여부만 return한다.
                # wishlist.rooms.delete()  # 리스트 추가 제거는 remove(), add()를 사용한다.
                wishlist.rooms.remove(room)
            else:
                wishlist.rooms.add(room)
            return Response(status=HTTP_200_OK)

Many-To-Many 관계 데이터
<https://docs.djangoproject.com/en/4.1/topics/db/examples/many_to_many/>

    rooms>serializers에 이미 좋아요 표시한 방을 볼 수 있도록 구현하겠다.
        is_liked = serializers.SerializerMethodField()

        def get_is_liked(self, room):
            request = self.context["request"]
            return Wishlist.objects.filter(
                user=request.user,
                rooms__pk=room.pk,  # model 객체의 컬럼을 검색하는 기능으로 '__컬럼명' 식으로 사용한다
            ).exists()


    방에 예약된 현황을 확인하는 페이지를 구현한다. (rooms/1/bookings)
    bookings>serializers 를 생성한다. 모든사람이 볼 수 있는 것(Public)과 방 주인만 볼 수 있는(Private) serializer를 생성해준다.

    예약된 현황을 오늘 이후의 값만 가져오도록 적용한다. python의 datetime 대신에 Django의 timezone을 사용한다.
        from django.utils import timezone
    config>settings 에 timezone 셋팅이 있다. 서버의 로컬타임 등 셋팅값이 포함되어 있다.
        TIME_ZONE = "Asia/Seoul"
        USE_TZ = True
    시간을 출력해본다.
        now = timezone(now)
        print(now())  # >>>: 2023-01-02 07:06:20.674650+00:00
                             [02/Jan/2023 16:06:20] "GET /api/v2/rooms/3/bookings HTTP/1.1" 200 7171  # 해당Text은 통신 프로토콜이다. django의 localtime이 출력된다.
    한국시간으로 출력이 되지 않는다. settings에 설정된 한국시간으로 표기할 수 있다.
        now = timezone.localtime
        print(now())  # >>>: 2023-01-02 16:10:46.105665+09:00
                             [02/Jan/2023 16:10:46] "GET /api/v2/rooms/3/bookings HTTP/1.1" 200 7171
    해당 데이터를 필터에 추가하여 오늘 이후의 예약현황을 가져오도록 하자.
        now = timezone.localtime().date()  # date(): 날짜만 가져온다.

        Bookings.objects.filter(
            ... ,
            check_in__gt=now,  # __gt: look up. line.391 참조
        )

    예약 기능을 구현한다. (rooms/1/bookings)
    bookings 모델에 check_in, check_out 은 필수값이 아니다.(이건 모델 설계의 실수이다).
    해당 값을 데이터를 받을때 필수값으로 하기위해선 serializerd에서 재정의가 필요하다.
        class CreateRoomBookingSerializer(...):
            check_in = serializers.DataField()

    serializer에서 데이터 검증 기능을 추가할 수 있다. 검증할 컬럼앞에 validate_ 를 붙여 함수를 구현한다.
    현재 날짜보다 이후의 날짜로 예약을 할 수 있도록 검증한다.
        def calidate_check_in(self, value):  # serializer호출할 때 해당 컬럼값을 이 함수에서 2번째 매개변수로 받는다.
            now = timezone.localtime().date()
            if now > value:
                raise serializers.ValidationError("Can't book in the past!")
            return value

    validate()를 통해 전체 데이터 검증도 가능하다.
        def validate(self, data):
            print(data)  # >>>: OrderedDict([('check_in', datetime.date(2023, 1, 25)), ('check_out', datetime.date(2023, 1, 31)), ('guests', 5)])
    체크인 날짜 이후에 체크아웃 날짜만이 가능하도록 기능을 추가한다.
        def validate(self, data):
            if data["check_in"] >= data["check_out"]:
                raise serializers.ValidationError(
                    "check out should be later than check in."
                )
            return data

    booking기간에 이미 booking이 있는지 체크 로직을 작성할 것이다. 우선 objects filter의 구현이다.
        Booking.objects.filter(
            check_in__gte=data["check_in"],
            check_out__lte=data["check_out"],
        ).exist()
    위 코드는 해당 범위 내 booking이 되어 있다면 잡아낼 것이다. 하지만 해당 범위에 벗어난 booking은 filter하지 못한다.
    만약 1일부터 7일까지 예약을 할때 이미 1일 부터 15일까지의 예약이 있다면 저 필터에 잡히지 않는다.
        Booking.objects.filter(
            check_in__lt=data["check_out"],  # 날짜 데이터는 늦은 날짜가 더 작다고 인식한다. == 체크인 보다 늦은 데이터["체크아웃"]
            check_out__gt=data["check_in"],  # 체크 인 뒤에 있는 booking이 체크인을 하면 안된다는 거다 내가 체크아웃하기전에.
        ).exist()
    예약할 booking check_in은 check_out을 서로 체크하면 날짜를 잡아낼 수 있다.

    view에서는 serializer.is_valid()를 사용하여 저장하는 기능을 구현하면 된다. user,room,kind 를 넣어준다.

## 12. Users API

#### [5_rest]

    Django앱에서 다루지 않은 user의 패스워드, 인증 기능들을 사용해볼 것이다.
    user의 자기 자신의 데이터를 확인 및 수정기능을 구현한다.


    user 회원가입 창을 구현한다. user의 패스워드를 받아서 해쉬값을 저장한다. row password를 저장해서는 안된다.
    - users>views -
        def post(self, request):
            password = request.data.get('password')
            if not password:
                raise ParseError()
            ...
            if serializer.is_valid():
                saved_user = serializer.save()
                saved_user.set_password(password)  # set_password(): 해쉬값으로 password값을 넣어준다.
                saved_user.save()
    추후에 비밀번호 인증기능을 추가할 수 있다.

#### ! url을 등록할때 변수를 받는 url은 같은레벨에 있는 url보다 밑에 위치를 시켜야한다.

    - users>urls -
        path("<str:username>", views.PublicUser.as_view()),
        path("me", views.Me.as_view()),
    url Me에 접근을 하여도 상단 <str:username> 로 판단하여 PublicUser로 접속된다.
    같은 레벨에 있는 url에서 최하단에 위치하다록 한다.
    ? 그럼 url에 포함된 username은 생성되지 못하도록 막아야 하나?. (이미 존재하는 username입니다. 이런식으로)
    그래서 이번 프로젝트에서는 인스타그램과 같이 username앞에 @를 붙여서 관리하도록 하겠다.
        path("@<str:username>", views.PublicUser.as_view()),

#### [5_Rest]

    타유저에게 보여줄 유저정보창을 구현한다.

    !! 코드챌린지 !!  더 커다란 user serializer를 만들어보자. user의 방 보유량 및 여행간 횟수 등등..


    user password 변경을 구현한다. 기존 패스워드와 새 패스워드를 받아서 값을 변경한다.
    - users>views -
        def put(self, request):
            user = request.user
            old_password = request.data.get("old_password")
            new_password = request.data.get("new_password")

            if user.check_password(old_password):  # check_password(): 해쉬값으로 비교하여 True,False를 반환한다.
                user.set_password(new_password)  # 꼭 hash값으로 넣어야한다.
                user.save()


    user의 login, logout 기능을 구현한다.
    login에 django에서 지원하는 함수를 사용한다.
        from django.contrib.auth import authenticate, login

        class LogIn(APIView):
            def post(self, request):
                username = request.data.get("username")
                password = request.data.get("password")
                ...

                user = authenticate(  # return user object
                    request,
                    username=username,  # 비교 요소
                    password=password,
                )
                if user:
                    login(request, user)  # 검증된 user 데이터로 로그인을 해준다.
                    ...

    logout도 django 함수를 이용하여 섹시하게(?) 기능구현이 가능하다.
        from django.contrib.auth import ... , logout

        class LogOut(APIView):

            permission_classes = [IsAuthenticated]

            def post(self, request):
                logout(request)  # post 프로토콜의 request값만으로 logout이 가능하다.
                ...

## 13. Check Point (Code Challenge)

    exerience 부분과 일부 user의 view, serializer부분을 추가해보자. react를 하고 나서 백엑드와 연결해야하는 부분에서 다시 작업을 해보자.

## 14. GraphQL API

    기초 개념을 배우고 나서 수강을 해야한다.

GraphQL로 영화 API 만들기
<https://nomadcoders.co/graphql-for-beginners/lobby>

    GraphQL로 영화 API 만들기 완강 후 빠른 시일에 학습하자.

## 15. Authenticated

    브라우져에서 사용할때 Django의 authentication 기능은 매우 훌륭하다. 하지만 브라우져외의 안드로이드 IOS에서의 보안은 취약하다.
    이번 섹션에서는 토큰, JWT(Json Web Token)같은 커스텀 인증을 구현해보겠다.

    request.data는 쿠키를 이용해 데이터를 인식한다. 이 방법을 views를 변경하지 않으며 토큰과 JWT 방식으로 변경헤 해본다.
        1. 멍청한 방법
        2. 토큰 방식
        3. JWT 방식
    으로 테스트를 해보겠다.

    postman을 설치한다. postman은 브라우져밖에서 API와 상호작용할때 사용된다.


    config>settings 에 Django_rest_framework의 default 인증방법을 명시하겠다.
        REST_FRAMEWORK = {
            'DEFAULT_AUTHENTICATION_CLASSES': [  # rest framework가 user를 찾는 방법들이 들어있다.
                'rest_framework.authentication.SessionAuthentication',  # 기본으로 이 한개가 들어있다.
            ]
        }
    입력하고 user창에 가도 이전과 같이 작동한다.

    rest_framework.authentication클래스에서 views로 request.user에 user데이터를 검증후 넣어준다.

    config내에 authentications.py를 생성해준다.
    첫번째로 안좋은 방법으로 검증하는 법을 구현해본다. 검증이 되면 user데이터를 반환하며 아닐경우 None을 반환한다.
        from rest_framework.authentication import BaseAuthentication

        class TruthMeBroAuthentication(BaseAuthentication):
            def authenticate(self, request):  # request에 쿠키와 헤더가 들어있다. user정보는 없다.
                print(request.headers)
                return None
    postman에서 GET http://127.0.0.1:8000/api/v2/users/me send한 데이터이다.
        print(request.headers)  # >>>: {'Content-Length': '', 'Content-Type': 'text/plain', 'User-Agent':
                'PostmanRuntime/7.29.2', 'Accept': '*/*', 'Postman-Token': '16c510b9-ba75-4a00-9de7-69be9c84a95b',
                'Host': '127.0.0.1:8000', 'Accept-Encoding': 'gzip, deflate, br', 'Connection': 'keep-alive'}
    postman에서 header에 데이터를 담아 보내본다. ("Trust-Me": "gh") Trust-Me 키가 있을경우 value값에 해당하는 유저가 있는지 찾아본다.
        username = request.headers.get("Trust-Me")
        if not username:
            return None
        try:
            user = User.objects.get(username=username)
            return (user, None)  # user데이터와 None을 같이 보내는 것이 규정이다.
        except User.DoesNotExist:
            raise AuthenticationFailed
    postman에서 ("Trust-Me": "gh") 헤더에 담아 보내면 user정보를 받을 수 있다.

    위방식은 누구인지 말만하면 해당 user로 검증이 되어서 사용이 가능하다. 물론 이방식을 쓰면 안된다.

    BasicAuthentication은 이전에 사용하던 로그인창이다.
    기본 브라우져에서 제공하던 로그인방식인데 login화면으로 이동하면 조그만창이 뜨면서 username과 password를 입력할 폼이 있다.

    token인식 방식을 구현해보겠다. token인증방식은 config>settings에 app추가로 구현가능하다. THIRD_PARTY_APPS에 추가하겠다.
        THIRD_PARTY_APPS = [
            ... ,
            "rest_framework.authtoken",
        ]
    이걸 추가하는걸로 admin페이지에서 token 모델을 볼 수 있다. 즉, 데이터베이스에 새로운 모델을 추가해줘야한다.
    INSERT_APPS에 추가될때 자동으로 makemigration 된다. migrate만 진행하면 된다.
    $ python manage.py migrate
    >>>: Running migrations:
           Applying authtoken.0001_initial... OK
           Applying authtoken.0002_auto_20160226_1747... OK
           Applying authtoken.0003_tokenproxy... OK
    token인증방식을 DEFAULT_AUTHENTICATION_CLASSES에 추가해준다.
        REST_FRAMEWORK = {
            "DEFAULT_AUTHENTICATION_CLASSES": [
                ... ,
                "rest_framework.authentication.TokenAuthentication",
            ]
        }
    token login방식을 사용할 url을 추가한다.
    - users>views -
        from rest_framework.authtoken.views import obtain_auth_token

        ...
            path("token-login", obtain_auth_token),
    obtain_auth_token views는 username, password를 보내면 token을 반환한다.
    postman으로 해당 url로 전송을 하며 body부분에 username과 password를 POST로 전송한다.
    token을 받는다. (참조 = 15.3_Token_Authentication_1.png)
    해당 토큰을 user한테 주며 데이터베이스에 저장하는 시스템으로 구성되어있다.

    토큰을 보내는 규칙이 있다. headers에 넣어주며 key - authorization에 토큰값을 넣어준다.
        authorization  -  Token [토큰값]
    이렇게 전송하는 것이 규칙이다.
    users.me 화면에 토큰전송 규칙으로 get 프로토콜을 보내면 내 user데이터를 받을 수 있다. (참조 = 15.3_Token_Authentication_2)
    그리고 admin에 token페이지를 가면 token이 등록되어 있다. 자동으로 데이터베이스에 넣어준것이다.
    해당 토큰을 삭제하면 더이상 그 토큰값으로 로그인이 되지 않는다. 토큰을 만료시킬 수 있는 것이다.!


    JWT(Json Web Token)을 구현해본다. JWT은 데이터베이스 공간을 사용하지 않는다.
    JWT를 사용하기 위해서 pyjwt를 설치해준다.
    $ poetry add pyjwt  # >>>: Installing pyjwt (2.6.0)

    users>urls에 url을 추가한다.
        path("jwt-login", views.JWTLogIn.as_view()),

    users>view에 클래스를 추가해준다. 기본 유저 검증 로직을 추가한다.
        class JWTLogIn(APIView):
            def post(self, request):
                username = request.data.get("username")
                password = request.data.get("password")
                if not username or not password:
                    raise ParseError

                user = authenticate(
                    request,
                    username=username,
                    password=password,
                )
    유저가 토큰에 사인하는 기능을 추가한다. 토큰은 암호화되어 있지만 내부데이터를 볼 수 있기때문에 중요한 정보는 넣지 않기로 한다.
    유저pk만 넣도록 구현해본다.
        import jwt
        from config import settings

        if user:
            token = jwt.encode(  # encode(): token화 한다.
                {"pk": user.pk},
                settings.SECRET_KEY,  # 비밀키로 서명. 나만 갖고 있는 유일한 키다.
                algorithm="HS256",  # 업계 표준 변경알고리즘
            )
            return Response({"token": token})
        else:
            return Response({"error": "Wrong password"})

    jwt-login url로 BODY - username,password를 POST 보내주면 새로운 토큰을 보내준다.
    토큰 길이가 훨씬길다. (참조 = 15.4 JWT Econde_1)

    JWT 토큰을 복호화하는 기능을 구현한다.
    config>Authentication 에 새 class를 만든다.
        class JWTAuthentication(BaseAuthentication):
            def authenticate(self, request):
                print(request.headers)
                return None
    해당 클래스를 config>settings 의 DEFAULT_AUTHENTICATION_CLASSES에 추가해준다.
    postman에서 이전에 받은 토큰을 이용해 users/me에 접속해본다.('jwt': [토큰값]) return이 none이기때문에 접속은 되지 않는다.
        print(request.headers)  # >>>: {'Content-Length': '47', 'Content-Type': 'application/json', 'jwt':
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwayI6Mn0.pOJaHhPoahf0n-L1VUyc9SI3dMQjjZcN09Vi6wzT2Es', 'User-Agent':
        'PostmanRuntime/7.29.2', 'Accept': '*/*', 'Postman-Token': '45865079-28ed-4102-9c4b-0946d4adbef5', 'Host':
        '127.0.0.1:8000', 'Accept-Encoding': 'gzip, deflate, br', 'Connection': 'keep-alive'}
    jwt 토큰값을 보낼때에는 value에 'token [토큰값]'형식이 아닌 그냥 토큰값을 보내면 된다.
    jwt복호화 기능을 구현한다.
        def authenticate(self, request):
            token = request.headers.get("jwt")
            decoded = jwt.decode(  # decode(): token을 복호화한다. encode()와 같게 넣어주면된다.
                token,
                settings.SECRET_KEY,
                algorithms="HS256",
            )
            print(decoded)  # >>>: {'pk': 2}
            return None
    postman에서 users/me로 토큰값과 함께 접근하면 user데이터가 출력된다.(decoded)
    pk로 user데이터를 찾아서 리턴해준다.
        pk = decoded.get("pk")
        if not pk:
            raise AuthenticationFailed("Invalid Token.")
        try:
            user = User.objects.get(pk=pk)
            return (user, None)  # user데이터와 None을 같이 보내줘야한다.
        ...


    비밀키를 settings파일에서 다른 파일로 옮기며 파일을 안보여주도록 적용한다.
    .env파일을 생성하여 secret key를 옮겨 준다.
        SECRET_KEY="django-insecure-..."
    .env파일을 작성할때 = 사이에 공백이 없어야한다!! ( [...]="..." ) 공백이 있으면 인식이 안됨
        SECRET_KEY = "..."  # <- X. 인식안됨
    해당파일을 gitignore에 추가하여 git에 올라가지 않도록 한다. (근데 이미 올렸다.)
    보안상으로는 공개하면 안되지만 연습용이기때문에 그대로 작업을 진행하겠다.

    .env를 읽는 django-environ 패키지를 설치한다.

<https://django-environ.readthedocs.io/en/latest/>

    $ poetry add django-environ
    config>settings 에 os와 environ을 import한다.
        import os
        import environ

        env = environ.Env()

        BASE_DIR = Path(__file__).resolve().parent.parent  # 기본으로 작성되어 있다.

        print(BASE_DIR)  # >>>: /Users/ghbyeon22/Documents/Develop/airbnb-clone/airbnb-clone-backend

        # environ.Env.read_env(f"{BASE_DIR}/.env")  # os.path.join()와 같은 결과값을 갖는다.
        environ.Env.read_env(os.path.join(BASE_DIR, ".env"))  # 읽을 파일로 추가
        print(os.path.join(BASE_DIR, ".env"))
        # >>>: /Users/ghbyeon22/Documents/Develop/airbnb-clone/airbnb-clone-backend/.env

        SECRET_KEY = env("SECRET_KEY")

        print(env("SECRET_KEY"))  # >>>: django-insecure-...
    .env에 변수를 추가하여 불러올때 변수명을 인수로 보내주면된다.

    다른 토큰인증 방법을 사용하고 싶다면 rest-framework사이트에서 확인 가능하다. django-rest-knox 를 추천(니꼬)

<https://www.django-rest-framework.org/api-guide/authentication/#third-party-packages>

    해당 프로젝트는 인증기능이 어떻게 작동되는지 확인하기위해 세부적으로 많이 코드를 작성했다.
    다음부터 인증기능을 구현할때는 simple JWT를 사용하도록 한다.

## 16. API Testing

#### [5_Rest]

    그동안 코드를 작성하고 수동으로 테스트를 진행했지만 자동으로 테스트를 해주는 코드를 작성한다.
    테스트에 필요한 규칙을 넣어놓기때문에 테스트 안정성이 높아진다.
    테스트 코드를 작성하기 앞서 해당 app의 views를 참조하여 에러가 발생할 부분을 체크하여 리스트화하자.
    로직에 오류가 발생하는 부분도 체크로직을 구성해야 오류를 확인 할 수 있다.
    로직의 오류나 실행여부와 상관없이 체크부분만 확인한다. 서버를 실행하고 있지않아도 테스트가 가능하다.

    rooms>tests 에서 작성한다. Django의 TestCase 대신 rest framework를 사용한다.
        from rest_framework.test import APITestCase
    테스트하고자 하는 대상을 test_를 붙여서 함수선언을 해줘야 실행이된다.

        class TestAmenities(APITestCase):

            def test_two_plus_two(self):
                self.assertEqual(first: Any, second: Any, msg: Any = ...)  # assert는 체크한다는 뜻이다.
                     # first, second를 체크하여 틀릴경우 msg가 출력됨.
    test명령어를 사용하여 테스트를 한다.
    $ python manage.py test
    >>>: Found 1 test(s).
        Creating test database for alias 'default'...
        System check identified no issues (0 silenced).
        .
        ----------------------------------------------------------------------
        Ran 1 test in 0.000s

        OK
        Destroying test database for alias 'default'...
    전체 앱에 테스트를 찾아서 실행해준다.
    대조값 두개를 틀리게 할경우 에러메세지다.
        Found 1 test(s).
        Creating test database for alias 'default'...
        System check identified no issues (0 silenced).
        F
        ======================================================================
        FAIL: test_two_plus_two (rooms.tests.TestAmenities)
        ----------------------------------------------------------------------
        Traceback (most recent call last):
        File "/Users/ghbyeon22/Documents/Develop/airbnb-clone/airbnb-clone-backend/rooms/tests.py", line 6, in test_two_plus_two
            self.assertEqual(2 + 2, 5, "The math is Wrong.")  # 내가 작성한 코드이다.
        AssertionError: 4 != 5 : The math is Wrong.

        ----------------------------------------------------------------------
        Ran 1 test in 0.000s

        FAILED (failures=1)
        Destroying test database for alias 'default'...
    값을 비교하기위해 자주 사용한다.


    self.client를 사용하여 url을 request할 수 있다. (client.login()으로 로그인도 할 수 있다.)
        class TestAmenities(APITestCase):
            def test_all_amenities(self):
                response = self.client.get("/api/v2/rooms/amenities/")
                print(response)  # >>>: <Response status_code=200, "application/json">
                print(response.json()) # >>>: []  # rooms/amenities에 값이 있어도 빈 list를 받는다.
    테스트를 할 때 console text를 보면 새 데이터베이스를 생성한다고 한다. 기존에 있는 데이터를 가져오지 않는다.
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "Response status code isn't 200.",
        )
        self.assertIsInstance(data, list)  # 데이터가 list의 instance인지 확인
    접속확인과 반환된 데이터 형식 테스트를 진행하였다.

    setUp()를 구현한다. setUp은 해당 클래스 내에 테스트 함수들보다 먼저 실행이 된다.
        NAME = "Amenity test"  # 재사용을 위해 전역변수로 생성
        DESC = "Amenity Des"

        def setUp(self):
            models.Amenity.objects.create(
                name=self.NAME,
                description=self.DESC,
            )
    들어온 데이터 검증 테스트.
        def test_all_amenities(self):
            ...
            self.assertEqual(
                len(data),  # 데이터 개수
                1,
            )
            self.assertEqual(
                data[0]["name"],
                self.NAME,
            )
            self.assertEqual(
                data[0]["description"],
                self.DESC,
            )


    데이터 생성 test를 진행한다.
        response = self.client.post(
            self.AMENITIES_URL,
            data={
                "name": "New Amenity",
                "description": "New Amenity desc.",
            },
        )
        self.assertEqual(
            response.status_code,
            200,
            "Create Failed.",
        )
    이때 response에는 방금 생성된 데이터만 들어있다.
    생성된 데이터를 검증한다.

    기존 views로직을 확인하면 serializer에서 오류가 발생하면 serializer오류 내역을 보내 준다.
    하지만 http프로토콜은 200을 전송하면서 정상신호로 받는다.
    해당부분을 테스트해본다.
        response = self.client.post(self.AMENITIES_URL)  # 데이터 생성에 amenity의 name은 필수값이다. serializer에 에러가 발생한다
        print(response)
        print(response.json())
    $ python manage.py test
    >>>: Found 2 test(s).
        Creating test database for alias 'default'...
        System check identified no issues (0 silenced).
        .<Response status_code=200, "application/json">
        {'name': ['이 필드는 필수 항목입니다.']}
        .
        ----------------------------------------------------------------------
        Ran 2 tests in 0.004s

        OK
        Destroying test database for alias 'default'...
    serializer에서 에러가 발생해도 http프로토콜은 200을 받는다.

    모든 app의 views 파일을 변경해줘야한다.
    - 모든 앱>views >  serializer 에러 전송부분 -
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    해당 프로토콜에 오류가 발생하는지 확인한다.
    - rooms>tests -
        response = self.client.post(self.AMENITIES_URL)
        self.assertEqual(
            response.status_code,  # >>>: 400
            200,
            "Post name is 필수",
        )
    에러가 발생한다. 데이터 검증을 추가한다.
        data = response.json()
        print(data)  # >>>: {'name': ['이 필드는 필수 항목입니다.']}
        # assertIn(member: Any, container: Iterable | Container, msg: Any = ...)
        self.assertIn("name", data)  # 값이 있다면 True
    오류메세지를 받기때문에 테스트에 오류가 발생하지 않는다.

    정상적인 데이터와 오류데이터를 테스트해보았다.


    Amenity 테스트를 진행한다. 새로운 클래스를 생성한다.
    test 클래스 하나가 실행이 끝날때마다 테스트 데이터베이스는 지워지며 다른 클래스가 실행될 때 새로 생성된다.
    그러므로 테스트 데이터를 다시 생성해준다.

## ! url주소 끝에 /를 제외하면 301에러를 반환한다.

    response = self.client.get("/api/v2/rooms/amenities/2")  # -> get(".../2/")
    print(response.status_code)  # >>>: 301

    근데 강의 영상에서는 끝에 /를 붙이지 않아도 오류가 발생하지 않는다. ??

#### [5_Rest]

    Amenity를 조회한 데이터는 queryset이 아닌 dictionary타입으로 데이터를 가져온다.
    get, delete를 구현한다. put기능은 코드 챌린지로 내가 작성해본다.
    지금까지는 views의 기능을 테스트해봤다. models의 데이터 제한에도 걸리는지 확인해볼 수 있다.


    인증 테스트를 구현해본다.(views Rooms) 해당 페이지는 IsAuthenticatedOrReadOnly 권한을 요구한다.
    인증이 안된 유저는 get 핸들러만 가능하며 post핸들러는 로그인한자만 가능하다.
    로그인을 하지 않고 rooms 생성로직을 작성한다.
        URL = "/api/v2/rooms/"

        def test_create_room_not_login(self):
            response = self.client.post(self.URL)

            self.assertEqual(response.status_code, 401)
    401(Unauthorized) 인증되지 않은 상태(로그인 X)를 반환한다.

    아이디를 생성하여 로그인 후 방 생성까지 테스트해본다.
        def test_create_room(self):
            user = User.objects.create(
                username="test",
            )
            user.set_password("123")
            user.save()

            self.client.login(
                username="test",
                password="123",
            )

            response = self.client.post(self.URL)
            print(response.status_code)  # >>>: 400
            print(response.json())
            # >>>: {'price': ['이 필드는 필수 항목입니다.'], 'rooms': ['이 필드는 필수 항목입니다.'], ...}
    필수값들을 넣지않아 room은 생성되지 않았지만 권한을 갖고 room생성 시도까지는 갈 수 있었다.

    비밀번호 생성없이 강제 로그인 기능이 있다.
        user = User.objects.create(
            username="test",
        )
        self.client.force_login(
            user,
        )
    단지 인증을 통과하기에는 이방식을 사용하는게 편리하다. 하지만 유저를 생성하는 url을 테스트한다면 사용기 어렵다.

## ! test 다른 앱도 구현해보기

    더 많은 assert기능들이 있으니 테스트를 구현하는데 여러가지를 시도해보자.
    틈틈히 다양한 방식으로 테스트를 해보며 프로그램 구동방식도 생각해보자.

## 17 Front-End SetUp

    드디어 프론트 엔드를 시작한다! create-react-app을 사용하며 chakra 라이브러리를 사용할 것이다.
    스크립트는 타입스크립트를 사용한다.

    우선 react를 설치한다.
    $ npm create-react-app airbnb-clone-frontend --templete=typescript
    # Happy hacking!


    18부터는 airbnb-clone-frontend 내 info에서 작성이 된다.

## 19 React Query

#### [2_Django]

    ...

    React 서버가 몇명 URL을 fetch하는 것을 허용해야한다.
    django-cors-headers를 설치해야한다. 서버에서 브라우져로 fetch할 수 있는 사람을 지정할 수 있다.

<https://github.com/AdamChainz/django-cors-headers/>
! 사이트 순서대로 설치하면 된다오!

    $ poetry add django-cors-headers

    corsheaders를 설치해준다.
        INSTALLED_APPS = [
            ...
            "corsheaders",
        ]
    미들웨어에도 추가해준다.
        MIDDLEWARE = [
            ...,
            "corsheaders.middleware.CorsMiddleware",
            # "django.middleware.common.CommonMiddleware",  # 이건 추가를 안한다?
        ]

    이제 settings파일에서 Configuration에 있는 속성들을 사용가능하다. CORS_ALLOWED_ORIGINS을 적용한다.
    - settings -
        CORS_ALLOWED_ORIGINS= ["http://localhost:3000"]  # 주소의 마지막 '/'는 지워줘야한다.
    react브라우져 검사창에서 CORS에러가 발생 안한다.

    방 리뷰 점수가 없을경우 'No Review'를 뜨도록하였는데 줄바뀜으로 예쁘지 않아서 0으로 변경.
    # #19.0 Manual Fetching_1 참조

    ...

## 19.4 Room Detail

기족에 room데이터에 좋아요 버튼에서 유저데이터를 가져와 좋아요를 한 room객체인지 확인하는 로직이 있다.
@rooms/serializers

    class RoomDetailSerializer(...):
        ...
        def get_is_liked(self, room):
            request = self.context["request"]
            return Wishlist.objects.filter(
                user=request.user,
                rooms__pk=room.pk,
            ).exists()

로그인안한상태에서 roomDetail객체를 확인하면 오류가 발생한다. 로그인을 안한 상태에서는 false를 반환한다.

    def get_is_liked(self, room):
        request = self.context["request"]
        if request.user.is_authenticated:
            return Wishlist.objects.filter(
                user=request.user,
                rooms__pk=room.pk,
            ).exists()
        return False

로그아웃한 상태에서도 room detail확인시 오류가 발생하지 않는다. -frontend 작업 계속

...

## 20 Authentication

### 20.1 Credentials

Django가 쓰는 url과 react가 쓰는 url이 다르기때문에 장고서버에서 react url로 쿠키가 전송되지 않는다. (도메인이 같지 않다.)
react페이지를 도메인을 갖게 적용을 하면 데이터를 가져올 수 없다. Django에서는 fetch가 가능한 도메인을 적용해야한다.

fetch가능한 도메인을 변경해준다.

    CORS_ALLOWED_ORIGINS = ["http://127.0.0.1:3000"]  # 포트는 리액트가 사용하는 3000으로 적용

Django에 설정을 추가해주면 아직 로그인을 확인하지는 못하지만 cookie에 sessionId 데이터가 추가된다.

...

Django에서 react에서 보내는 credential을 받도록 적용해야한다.

@config/settings.py

    CORS_ALLOW_CREDENTIALS = True

react페이지에서 로그인 확인이 가능하다.

...
