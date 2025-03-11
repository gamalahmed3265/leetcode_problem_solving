مكملين معاكم و معانا نهارده مسائله

125. Valid Palindrome

المسائله بختصار هيبقى فى str يحتوي على on-alphanumeric

و alphanumeric و number

و انت دورك تعمل filter ل alphanumeric و number يعنى تحذف , : ? , .....

زي المثال

```python
    s = "A man, a plan, a canal: Panama"
```

مطلوب منك ترجع حروف الابجاديه و الارقام و تحولهم الى lowercase

---

الحقيقه فى اكتر من طريقه

مثلا لو تشغل ب python هتقعد كل اشويه تعمل replace ل

زي كدا

```python
    s=s.replace(",","").replace(":","").lower()
```

بس فى حل افضل بكتير زي انى استعمل regular expression

زي

```python
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
```

هنا بقوله خد بس الحروف من a الى z , من A الى Z , من 0 الى 9

و حولهم الى lower case

, بعدين ب check حل هو palindrome و لاء

يعنى ايه palindrome

هو انك تقراء ال str من الاول الى الاخر و عكس صحيح

```python
    rs==rs[::-1]
```

و خلاص كدا ي معلم

دعمك بلايك و شير علشان نكمل و يبقى فى محتوي عربى قوي

[Problem](https://leetcode.com/problems/valid-palindrome/)
