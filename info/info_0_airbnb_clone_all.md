[1_python]

    일부 운영체제에서는 호환성때문에 python명령어를 사용하면 python2로 접속이 된다. python2는 사용하면 안되며 python3를 사용해야 한다.
    $ python3

    git을 생성 및 초기화
    $ git init

[2_Django]

    패키지 설치 및 관리를 위해 poetry를 사용한다.(=pip) pip보다 관계관리에 편리하다.
    poetry를 설치한다. <https://python-poetry.org/docs>
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
        다른 설정 방법 확인은 <https://docs.djangoproject.com/en/4.1/ref/models/fields/>
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
        그외의 설정방법은 <https://docs.djangoproject.com/en/4.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields>
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
        더보기. <https://docs.djangoproject.com/en/4.1/ref/contrib/admin/#modeladmin-options>

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
    더보기. <https://docs.djangoproject.com/en/4.1/ref/models/fields/#choices>


    rooms app을 설치한다.(startapp -> settings설치)
    model,admin 구현 후 migrate 하기로 한다.

    country와 city를 위한 package가 있다. 추후에 적용할 예정이다. TextChoices ?

    Room 모델을 구현후 amenity도 구현한다. rooms와 amenity는 many-to-many 관계를 갖는다.
    many-to-many는 room에서 여러 Amenity를 등록할 수 있다. many-to-many는  Foriegn과 다르게 on_delete값이 필수가 아니다.

    만들어진 날짜와 수정된 날짜를 추가해준다.
        created = models.DateTimeField(auto_now_add=True)
        # <https://docs.djangoproject.com/en/4.1/ref/models/fields/#datetimefield>
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
    # <https://zetawiki.com/wiki/%ED%8C%8C%EC%9D%B4%EC%8D%AC_title()>
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