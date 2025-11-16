# مستخرج الجذور / Root Extractor

<div dir="rtl">

## نظرة عامة

أداة بسيطة وفعالة لاستخراج الجذور من الفروع الصرفية العربية. تحلل الكلمات وفق الأوزان الصرفية وتستخرج الجذور الثلاثية والرباعية.

## المميزات

- 🔍 **استخراج الجذور**: استخراج الجذور من الفروع الصرفية
- 📝 **دعم الأوزان**: دعم الأوزان الثلاثية والرباعية
- ⚡ **معالجة سريعة**: معالجة سريعة للملفات النصية
- 📄 **صيغة بسيطة**: صيغة إدخال وإخراج بسيطة

## التثبيت

### المتطلبات

- Python 3.7 أو أحدث

### خطوات التثبيت

1. استنسخ المستودع:
```bash
git clone https://github.com/ayzem88/root-extractor.git
cd root-extractor
```

2. قم بتشغيل البرنامج مباشرة:
```bash
python "المحلل الجذري.py"
```

## الاستخدام

1. ضع الفروع في ملف `الفروع.txt` بالصيغة: `وزن = كلمة`
2. قم بتشغيل البرنامج:
```bash
python "المحلل الجذري.py"
```

3. سيتم إنشاء ملف `الجذور.txt` بالجذور المستخرجة

## هيكل المشروع

```
مستخرج الجذور/
├── المحلل الجذري.py          # البرنامج الرئيسي
├── الفروع.txt                # ملف الفروع المدخل
└── الجذور.txt                # ملف الجذور الناتج
```

## الملفات الرئيسية

- **المحلل الجذري.py**: البرنامج الرئيسي لاستخراج الجذور

## مثال على الصيغة

**الإدخال (الفروع.txt)**:
```
فَعَلَ = كَتَبَ
مَفْعُول = مَكْتُوب
```

**الإخراج (الجذور.txt)**:
```
ف ع ل = ك ت ب
ف ع ل = ك ت ب
```

## ملاحظات مهمة

⚠️ **ملاحظة**: 
- ملف الإدخال يجب أن يكون بصيغة: `وزن = كلمة`
- كل سطر يحتوي على وزن وكلمة واحدة

## التطوير المستقبلي

- [ ] واجهة رسومية (GUI)
- [ ] دعم المزيد من الأوزان
- [ ] معالجة متقدمة للجذور المعتلة
- [ ] تصدير النتائج بصيغ متعددة

## المساهمة

نرحب بمساهماتكم! يرجى قراءة [CONTRIBUTING.md](CONTRIBUTING.md) للمزيد من التفاصيل.

## الترخيص

هذا المشروع مخصص للاستخدام الأكاديمي والبحثي.

## منهج التطوير

أُعتمد في مشاريعي البرمجية على منهج Vibe Coding؛ أسلوب يتجاوز كتابة كلّ سطر يدوياً، إذ أوجّه نماذج الذكاء الاصطناعي بوصف منطقي وواضح للوظيفة المطلوبة، ثم أُقيّم النتائج وأُدخِل التحسينات.

هذا النهج يعزّز السرعة في إنشاء النماذج الأولية والوِحدات البرمجية، ويمنحني تركيزاً أكبر على التصوّر العام والتصميم بدلاً من التفاصيل الدقيقة.

في هذا المستودع، تجد أدوات ومشاريع بُنيت بهذه المقاربة — يُرحّب بتجربتها والمساهمة فيها.

## المطور

تم تطوير هذا المشروع بواسطة **أيمن الطيّب بن نجي** ([ayzem88](https://github.com/ayzem88))

---

# [English]

<div dir="ltr">

## Overview

A simple and efficient tool for extracting roots from Arabic morphological branches. Analyzes words according to morphological patterns and extracts trilateral and quadrilateral roots.

## Features

- 🔍 **Root Extraction**: Extract roots from morphological branches
- 📝 **Pattern Support**: Support for trilateral and quadrilateral patterns
- ⚡ **Fast Processing**: Fast processing of text files
- 📄 **Simple Format**: Simple input and output format

## Installation

### Requirements

- Python 3.7 or later

### Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/ayzem88/root-extractor.git
cd root-extractor
```

2. Run the program directly:
```bash
python "المحلل الجذري.py"
```

## Usage

1. Place branches in `الفروع.txt` file in format: `pattern = word`
2. Run the program:
```bash
python "المحلل الجذري.py"
```

3. The `الجذور.txt` file will be created with extracted roots

## Project Structure

```
root-extractor/
├── المحلل الجذري.py          # Main program
├── الفروع.txt                # Input branches file
└── الجذور.txt                # Output roots file
```

## Main Files

- **المحلل الجذري.py**: Main program for root extraction

## Format Example

**Input (الفروع.txt)**:
```
فَعَلَ = كَتَبَ
مَفْعُول = مَكْتُوب
```

**Output (الجذور.txt)**:
```
ف ع ل = ك ت ب
ف ع ل = ك ت ب
```

## Important Notes

⚠️ **Note**: 
- Input file must be in format: `pattern = word`
- Each line contains one pattern and one word

## Future Development

- [ ] Graphical user interface (GUI)
- [ ] Support for more patterns
- [ ] Advanced processing for weak roots
- [ ] Export results in multiple formats

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## License

This project is intended for academic and research use.

## Development Approach

I adopt the Vibe Coding paradigm in my software projects: rather than writing every line manually, I direct AI models with clear natural-language descriptions of the desired functionality, then evaluate and refine the generated code.

This approach accelerates prototype and module creation, allowing me to focus more on concept and design than on low-level implementation details.

In this repository you'll find tools and projects developed with this mindset — feel free to explore and contribute.

## Developer

Developed by **Ayman Atieb ben NJi** ([ayzem88](https://github.com/ayzem88))

</div>

