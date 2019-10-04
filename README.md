# create_invoices
Приложение для просмотра накладных и скачивания их в формате .docx

##Как развернуть проект:
Клонируем проект
```
git clone https://github.com/metro6/create_invoices.git
cd create_invoices
```
Создаем виртуальное окружение и активируем его
```
python3 -m venv venv
source/bin/activate
```
Устанавливаем зависимости проекта
```
pip install -r requirements.txt
```
Переходим в каталог проекта, применяем миграции
```
cd create_invoices
./manage.py migrate
```
Создаем суперпользователя
```
./manage.py createsuperuser
```
И следуем интерактивным подсказкам

Проект Готов!
Для запуска проекта:
```
./manage.py runserver
```
Приложение стартует по адресу http://localhost:8000

Далее, заходим в админку по адресу http://localhost:8000/admin, создаем новую форму продуктов и переходим на сайт 
http://localhost:8000 

###В проекте используются:
- django 
- python-docx (https://python-docx.readthedocs.io/en/latest/index.html)
- sqlite
- jquery, jquery-datetimepicker

Для проекта были созданы фикстуры (с ними можно не применять миграции и не создавать пользователя)

https://drive.google.com/file/d/1sFnQgMygxvNaAa2qBGU2pXSejseNcA6o

Содержимое каталога fixtures нужно переместить в каталог create_invoices в корне проекта

Логин/Пароль администратора Admin/admin