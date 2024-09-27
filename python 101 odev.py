import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dosya_yolu = 'c:\\Users\\EFE\\Desktop\\Housing.csv'

df = pd.read_csv(dosya_yolu)

if df.empty:
    print("Veri seti boş, lütfen kontrol edin.")
else:
    print("Veri seti başarıyla yüklendi.")

print("Eksik değerler:\n", df.isnull().sum())

plt.figure(figsize=(14, 6))

plt.subplot(1, 3, 1)
plt.hist(df['area'].dropna(), bins=30, edgecolor='black', alpha=0.7)
plt.title("Ev Alanı Dağılımı")
plt.xlabel("Alan (m²)")
plt.ylabel("Ev Sayısı")
plt.grid(axis='y')

plt.subplot(1, 3, 2)
plt.hist(df['bedrooms'].dropna(), bins=10, edgecolor='black', alpha=0.7)
plt.title("Oda Sayısı Dağılımı")
plt.xlabel("Oda Sayısı")
plt.ylabel("Ev Sayısı")
plt.grid(axis='y')

plt.subplot(1, 3, 3)
plt.hist(df['stories'].dropna(), bins=5, edgecolor='black', alpha=0.7)
plt.title("Kat Sayısı Dağılımı")
plt.xlabel("Kat Sayısı")
plt.ylabel("Ev Sayısı")
plt.grid(axis='y')

plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='price', hue='area', bins=30, element='step', stat='density', common_norm=False, palette='viridis')
plt.title("Ev Fiyatları ile Alan İlişkisi")
plt.xlabel("Fiyat (Dolar)")
plt.ylabel("Yoğunluk")
plt.legend(title='Alan (m²)', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(axis='y')
plt.show()

plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='price', hue='bedrooms', bins=30, element='step', stat='density', common_norm=False, palette='viridis')
plt.title("Ev Fiyatları ile Oda Sayısı İlişkisi")
plt.xlabel("Fiyat (Dolar)")
plt.ylabel("Yoğunluk")
plt.legend(title='Oda Sayısı', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(axis='y')
plt.show()

plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='price', hue='stories', bins=30, element='step', stat='density', common_norm=False, palette='viridis')
plt.title("Ev Fiyatları ile Kat Sayısı İlişkisi")
plt.xlabel("Fiyat (Dolar)")
plt.ylabel("Yoğunluk")
plt.legend(title='Kat Sayısı', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(axis='y')
plt.show()

ortalama_banyo_fiyatı = df.groupby('bathrooms')['price'].mean()
ortalama_banyo_fiyatı.plot(kind='bar', color='lightblue', figsize=(8, 6))
plt.title("Banyo Sayısına Göre Ortalama Ev Fiyatı")
plt.xlabel("Banyo Sayısı")
plt.ylabel("Ortalama Fiyat (Dolar)")
plt.xticks(rotation=0)
plt.show()

ortalama_eşya_fiyatı = df.groupby('furnishingstatus')['price'].mean()
ortalama_eşya_fiyatı.plot(kind='bar', color='lightgreen', figsize=(8, 6))
plt.title("Eşya Durumuna Göre Ortalama Ev Fiyatı")
plt.xlabel("Eşya Durumu")
plt.ylabel("Ortalama Fiyat (Dolar)")
plt.xticks(rotation=0)
plt.show()

korelasyon_matrisi = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(korelasyon_matrisi, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Korelasyon Matrisi")
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x='area', y='price', data=df)
plt.title("Ev Alanı ile Fiyat İlişkisi")
plt.xlabel("Alan (m²)")
plt.ylabel("Fiyat (Dolar)")
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x='bedrooms', y='price', data=df)
plt.title("Oda Sayısı ile Fiyat İlişkisi")
plt.xlabel("Oda Sayısı")
plt.ylabel("Fiyat (Dolar)")
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x='stories', y='price', data=df)
plt.title("Kat Sayısı ile Fiyat İlişkisi")
plt.xlabel("Kat Sayısı")
plt.ylabel("Fiyat (Dolar)")
plt.grid(True)
plt.show()