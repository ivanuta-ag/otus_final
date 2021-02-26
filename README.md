# Otus_final_project
1. Установить зависимости:
	pip install -r requirements.txt
	
2. Параметры запуска:
	pytest --alluredir allure-results  (для формирования отчета allure)
	--browser=chrome (по умолчанию)
	--browser=firefox
	--browser=remote (selenium-server)
	--browser=remote_selenoid (selenoid )