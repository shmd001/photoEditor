# photoEditor

Фоторедактор, реализованный на Python + PyQt5

## Developers Team:
    1. Maintainer - 2020-5-24-sho
    2. Developer - 2020-5-21-tak
    3. Developer - 2020-5-01-abr
    4. Developer - 2020-5-23-shi

## Цели:
    1. Выкатить первую версию фоторедактора, обладающего примитивным функционалом
    2. Протестировать

### Задачи для maintainer:
* [x] Добавить README.md с текущими целями
* [x] Добавить requirements.txt, со списком всех библиотек, используемых в проекте
* [x] Пересобрать главный класс фоторедактора, сделать формирование дизайна функционально
* [x] Реализовать ```createMainLabel()```, рисующую главный label
* [x] Убрать ненужный функционал при открытии главного окна приложения
* [x] Написать стили для текущих компонентов, удобно расположить компоненты на окне

### Задачи для developer-2:
* [x] Реализовать запуск окна, согласно дизайну 
* [x] Реализовать ```createEditingBar```, рисующую панель редактирования
* [x] Привести названия переменных и функций к единому стилю 
* [ ] Реалзовать открытие файла

### Задачи для developer-3:
* [x] Сфорировать **design.py** согласно **design.ui**
* [x] Реализовать ```createMenu```, рисующую меню
* [x] Покрыть код комментариями  

### Задачи для developer-4:
* [x] Задизайнить окно фоторедактора в QT Designer, на выходе **design.ui**
* [x] Реализовать ```createToolBar```, рисующую панель инструментов
* [x] Разбить ```main.py``` на несколько файлов
* [ ] Реализовать закрытие приложения нажатием на кнопку

### Задачи на перспективу:
* [ ] Сформировать *about* и реализовать в виде MessageBox принажатии на кнопку в меню

### Соответствие Qactions и методов класса, которые для них используются
about_act => ```aboutDialog()```  
exit_act => ```close()```  
open_act => ```image_label.openImage()```  
save_act => ```image_label.saveImage()```  
revert_act => ```image_label.revertToOriginal()```  
crop_act => ```image_label.cropImage()```  
resize_act => ```image_label.resizeImage()```  
rotate90_cw_act => ```image_label.rotateImage90("cw")```  
rotate90_ccw_act => ```image_label.rotateImage90("ccw")```  
flip_horizontal => ```image_label.flipImage("horizontal")```  
flip_vertical => ```image_label.flipImage("vertical")```  
zoom_in_act => ```zoomOnImage(1.25)```  
zoom_out_act => ```zoomOnImage(0.8)```  
normal_size_act => ```normalSize()```  
