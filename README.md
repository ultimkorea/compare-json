# compare-json

## Задача: Сравнить два json'а. 

- объекты в JSONе сравниваются по ключу "type"

### В каталоге compare по окончанию создается файл log.txt 
- выводятся новые ключи в *_TS
- выводятся отсутствующие ключи в *_TS
- выводятся изменения в значении ключей

### Как пользоваться?
1. Файлы, которые сравниваете, положите на один уровень со скриптом
2. Названия = filename_TS.json (основной), и filename_XML.json
3. Запустите скрипт

### Пример JSON: 
```javascript
 [{
    "type": "unique_type1",
    "message0": "message",
    "args0": [
      {
        "type": "input_value",
        "name": "NAME",
        "check": "String",
        "align": "RIGHT"},
      {
        "type": "input_value",
        "name": "VALUE",
        "check": "String",
        "align": "RIGHT"}],
    "previousStatement": null,
    "nextStatement": null,
    "style": "style",
    "tooltip": "BlockType: unique_block",
    "helpUrl":
      "https://url.ru"},
  {
    "type": "unirue_type2",
    "message0": "message",
    "args0": [
      {
        "type": "input_value",
        "name": "NAME",
        "check": "String",
        "align": "RIGHT"}],
    "output": null,
    "style": "style",
    "tooltip": "BlockType: unique_block2",
    "helpUrl":
      "https://url.ru"}]
```

### Пример лога
```
Type 'unique_block1': Changes found - New keys in TS: message0
Type 'unique_block3': OK
Type 'unique_block4': OK
Type 'unique_block5' not found in XML JSON.
Type 'unique_block6': Changes found - helpUrl: 'https://url.ru/12345' -> 'https://url.ru/123456789', New keys in TS: style
Type 'unique_block7': Changes found - New keys in TS: style
Type 'unique_block8': Changes found - helpUrl: '' -> 'https://url.ru/123', Missing keys in TS: colour, New keys in TS: style
Type 'unique_block9': Changes found - helpUrl: '' -> 'https://url.ru', Missing keys in TS: colour, New keys in TS: style
Type 'unique_block10': Changes found - Missing keys in TS: colour, New keys in TS: style
```
