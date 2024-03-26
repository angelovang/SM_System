# SM_System
Service management system
Система за управление на компютърен сервиз

1. Примерна организация на сервизната дейност 
	
Стъпка 1 :
  Клиента пристига в сервиза с повреденото устройство/ва
  Приемчик :
  Приема устройството и създава сервизна карта (или работна карта/поръчка), която има ID , дата на приемане и статус чакаща.
  Попълва данните за клиента ( име , имейл, телефон )
  Попълва данните за устройството ( вид – PC,Laptop,Monitor,Printer ;
  производител , модел, сериен № ; описание на повредата.
  Разпечатва ID то на сервизната карта и го прикрепва към устройството.
  Разпечатва разписка за клиента с която да си получи устройството след ремонта или да може да проверява на сайта статуса на поръчката.
	
Стъпка 2:
  Сервизен техник / инженер :
  Влиза в списъка с поръчките и избира поредната поръчката
  Въвежда старт на поръчката , тя се присвоява на негово име и стуса става на „in progress“
  Извършва ремонта
  Влиза в списъка с поръчките
  Дава край на поръчката
  Попълва описание на ремонта и вложените материали

Стъпка 3:
  Генерира се е-мейл/СМС за клиента / приемчика го уведомява по телефона , че поръчката е готова

Стъпка 4:
  Клиента идва в сервиза и представя разписката
  Приемчика я идентифицира , издава касов документ с списък от вложените материали и труда за ремонта. Ако има необходимост може да добави коментар.
  Клиента заплаща ремонта и получава устройството

2. Потребители на системата
  Администратор – не е задължително да работи в сервиза – superuser
  Приемчик – логва се от страна на сайта (username, password) и може да създава, редактира, и приключва сервизните карти, или да ги трие 
  Сервизен техник – логва се от страна на сайта (username, password), стартира и приключва ремонта и попълва данни за материалите  
  Клиент – логва се с телефонен № и ID на поръчка – получава информация за статуса на поръчката и ако е приключила за материали, труд и цена
  ??? Мениджър – логва се от страна на сайта (username, password) – може да следи списъка с поръчките – за определен период , материалите, брой изпълнени поръчки по служители, склад материали .

3. Модели / таблици на DB
  Потребители – ID, username, email, password, first_name, last_name, user_type
  Клиенти – id, first_name, last_name, email, phone, servise_card_id
  Сервизна карта – id, client_id , device_type,  manufacturer, serial_number, 
  problem_description, accept_date, rep_start_date, rep_end_date, repair_description, price, compl_date, status
  Работна карта – id, sk_id, device_type, problem_desscription, rep_start_date, rep_end_date, repair_description, tenician_id , price , ... ???

4. Страници на сайта
   
Home_page – фон на сайта , лого на фирмата, нещо за фирмата , меню лента, в менюто да има възможност за вход за клиенти , вход за служители, футър
Client page – форма за проверка статуса на поръчката
Staf_page – форма за login , register
Dashboard – регистрация или избор на клиент, създаване , редактиране на заявки
Repair/work order – стартиране, приключване на заявка
Statistic – статистическа информация за мениджъри

6. URL адреси :
	
