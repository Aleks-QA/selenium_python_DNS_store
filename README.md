<h3 tabindex="-1" dir="auto">Проект по автоматизации тестирования DNS-SHOP</h3>
<hr>
<h4 dir="auto"><em>О проекте:</em></h4>
<ol>
<li dir="auto">В процессе теста происходит оформления заказа в интернет-магазине:</li>
  <ul dir="auto">
    <li>Авторизация,</li>
    <li>Из выпадающего меню выбирается категория, </li>
    <li>Добавляются различные фильтры,</li>
    <li>На каждом этапе покупки сверяем название и цену,</li>
    <li>В конце происходит очистка корзины,</li>

  </ul>
    <li>Проект построен используя принципы ООП и POM,</li>
    <li>Добавлено логирование и отчеты Allure.</li>
</ol>

<hr>

<h4 dir="auto"><em>Для запуска тестов необходимо:</em></h4>
<ol>
  <li>Скачать проект с удаленного репозитория на свой локальный, с помощью команды:<br>
    <code>git clone https://github.com/Aleks-QA/selenium_python_DNS_store.git</code></li>
  
  <li>Открыть проект на установленной заранее IDE</li>
  
  <li>Создать и активировать виртуальное окружение:</li>
    <code>python -m venv venv</code></li><br>
    <code>venv\Scripts\activate</code></li>
    
  <li>Установить все зависимости: <br>
  <code>python -m pip install -r requirements.txt</code> 
      
  <li>Запустить тесты командой:<br><code>python -s -m pytest --alluredir=test_results</code> </li>
  
  <li>Открыть отчет о прохождении тестов командой:<br>
    <code>allure serve test_results/ </code></li>
</ol>


