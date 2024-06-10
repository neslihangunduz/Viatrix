import os
import io
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
import fitz  # this is pymupdf
from PIL import Image
import PIL
#
load_dotenv()
genai.configure(api_key="AIzaSyCIyVGIaXqM4oMfH-KnjQdHDQPoiNyTFpI")


@st.cache_resource
def get_gemini_response(prompt):
    # Modelin Ayar Kısmı
    generation_config = {
        "temperature": 0.9,
        "top_p": 0.90,
        "top_k": 64,
        "max_output_tokens": 18192,
        "response_mime_type": "text/plain",
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
    ]

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash-latest",
        safety_settings=safety_settings,
        generation_config=generation_config,
    )

    prompt_token_count = model.count_tokens(prompt)

    response = model.generate_content(prompt)

    st.markdown(response.text)

    response_token_count = model.count_tokens(response.text)

    return response, prompt_token_count, response_token_count


st.set_page_config(
    page_title="RoamGuide",
    page_icon="🗺️",
    initial_sidebar_state="expanded"
)


@st.cache_resource
def load_image(image_file):
    img = Image.open(image_file)
    return img


menu = ["Ana Sayfa", "Viatrix", "Forum & Tartışma", "Hadi Bi'yerlere Gidelim!", "Yol Manzaraları", "Aramıza Katılın!"]
choice = st.sidebar.selectbox("Menü", menu)
cacha_image = st.sidebar.image("cache.png", caption='"Hadi Dünyayı Küçültelim!"')

if choice == "Ana Sayfa":
    st.title("KEŞİF YOLUNDA")

    @st.cache_resource
    def load_image(image_file1):
        img1 = Image.open(image_file1)
        return img1

    image_file_path1 = "C:\\Users\\nesli\\PycharmProjects\\RoamGuide\\dünya_haritası.png"
    image1 = load_image(image_file_path1)

    # Streamlit arayüzünde görüntüyü gösterme
    st.image(image1)
    st.subheader(
        '"Yolculuk, bir noktadan diğerine gitmek değil, öğrenmek, keşfetmek ve değişmektir." \n – Ursula K. Le Guin')
    st.subheader('Neden Seyahat Edip Maceraya Atılmalısınız?')
    st.write("""
Yeni Ufuklar Keşfetmek
Dünyamız muhteşem ve çeşitliliklerle dolu. Farklı kültürler, insanlar ve doğal güzellikler keşfetmek, hayatınıza derinlik ve zenginlik katacaktır. Her yeni yer, her yeni insan, farklı bir bakış açısı, farklı bir hikaye demektir. Seyahat etmek, kendinizi ve dünyayı daha iyi anlamanızı sağlar.

Kişisel Gelişim ve Öz Güven Artışı
Seyahat etmek, konfor alanınızdan çıkmanızı gerektirir. Yeni yerlerde yeni insanlar tanımak, yeni diller öğrenmek ve farklı kültürel normlara adapte olmak, kişisel gelişiminize büyük katkı sağlar. Zorluklarla başa çıkmayı öğrenmek, problem çözme yeteneklerinizi geliştirir ve özgüveninizi artırır.

Stresten Arınma ve Ruhsal Yenilenme
Günlük yaşamın stresi, iş yükü ve rutininden kaçmak, zihinsel ve ruhsal sağlığınız için önemlidir. Seyahat, bu streslerden uzaklaşmanızı ve zihinsel olarak yenilenmenizi sağlar. Doğayla iç içe olmak, tarihi yerler keşfetmek veya sadece yeni bir şehirde kaybolmak bile ruhunuza iyi gelecektir.

Yeni Beceriler Kazanma
Seyahat ederken, yeni beceriler kazanmanız kaçınılmazdır. Bu, yeni bir dil öğrenmekten, farklı yemek tarifleri denemeye kadar geniş bir yelpazeyi kapsar. Ayrıca, seyahat planlaması yaparken organizasyon ve bütçe yönetimi gibi pratik beceriler de kazanırsınız.

Kültürel Farkındalık ve Hoşgörü
Dünyanın farklı yerlerindeki insanların yaşam biçimlerini, inançlarını ve geleneklerini gözlemlemek, kültürel farkındalığınızı artırır. Bu da hoşgörü ve empati gibi değerli erdemleri geliştirir. Farklı kültürleri anlamak, onları daha iyi tanımak, dünya vatandaşlığı bilincinizi güçlendirir.

Unutulmaz Anılar ve Bağlantılar
Seyahat ederken yaşadığınız her anı, unutulmaz anılar biriktirmenizi sağlar. Bu anılar, hayatınız boyunca sizinle kalacak ve geri dönüp baktığınızda yüzünüzde bir gülümseme oluşturacaktır. Ayrıca, seyahat sırasında tanıştığınız insanlar, ömür boyu sürecek dostlukların kapısını aralayabilir.

Kendinizi Tanıma Fırsatı
Seyahat etmek, kendinizi keşfetmek için eşsiz bir fırsattır. Yeni ortamlarda ve durumlarda nasıl tepki verdiğinizi görmek, kendi sınırlarınızı ve yeteneklerinizi anlamanızı sağlar. Seyahat, kim olduğunuzu, ne istediğinizi ve hayatınızı nasıl şekillendirmek istediğinizi anlamanıza yardımcı olur.

İlham ve Yaratıcılık
Farklı yerlerde farklı deneyimler yaşamak, ilham ve yaratıcılığınızı artırır. Yeni manzaralar, sesler ve kokular, hayal gücünüzü besler ve yaratıcılığınızı tetikler. Bu, özellikle sanatçılar, yazarlar ve yaratıcı mesleklerde çalışanlar için önemlidir.

Seyahat etmek, sadece yeni yerler görmek değil, aynı zamanda kendinizi keşfetmek, dünyayı anlamak ve hayatınıza zenginlik katmaktır. Her yolculuk, kendinizi ve dünyayı yeniden keşfetmek için bir fırsattır. Maceraya atılın ve bu büyüleyici yolculuğun tadını çıkarın!
        """)

if choice == "Viatrix":
    st.title("Viatrix")

    @st.cache_resource
    def load_image(image_file2):
        img2 = Image.open(image_file2)
        return img2

    image_file_path2 = "C:\\Users\\nesli\\PycharmProjects\\RoamGuide\\Seyyah.png"
    image2 = load_image(image_file_path2)

    # Streamlit arayüzünde görüntüyü gösterme
    st.image(image2)
    st.subheader('"Seyahat etmek, kendi hikayenizi yazmaktır." \n - Anonim')

    st.write("")

    # Şehir listesi (Şehir ekle)
    cities = ['Adana', 'Adıyaman', 'Afyonkarahisar', 'Ağrı','Aksaray','Amasya','Ankara','Antalya','Ardahan','Artvin',
              'Aydın','Balıkesir','Bartın','Batman','Bayburt','Bilecik','Bingöl','Bitlis','Bolu','Burdur','Bursa',
              'Çanakkale','Çankırı','Çorum','Denizli','Diyarbakır','Düzce','Edirne','Elazığ','Erzincan','Erzurum',
              'Eskişehir','Gaziantep','Giresun','Gümüşhane','Hakkâri','Hatay','Iğdır','Isparta','İstanbul','İzmir',
              'Kahramanmaraş','Karabük','Karaman','Kars','Kastamonu','Kayseri','Kilis','Kırıkkale','Kırklareli',
              'Kırşehir','Kocaeli','Konya','Kütahya','Malatya','Manisa','Mardin','Mersin','Muğla','Muş','Nevşehir',
              'Niğde','Ordu','Osmaniye','Rize','Sakarya','Samsun','Şanlıurfa','Siirt','Sinop','Sivas','Şırnak',
              'Tekirdağ','Tokat','Trabzon','Tunceli','Uşak','Van','Yalova','Yozgat','Zonguldak'
              ]


    selected_city = st.selectbox('Şehir Seçin', cities)
    selected_spots = st.text_input('Hangi harika yerleri keşfetmek istiyorsunuz?', placeholder='Bir yer adı yazın...')

    st.write('Seçilen şehir:', selected_city)

    # Seçilen şehre göre turistik yer listesi

        #'İstanbul': ['Ayasofya', 'Topkapı Sarayı', 'Sultanahmet Camii'],
        #'Ankara': ['Anıtkabir', 'Etnografya Müzesi', 'Atatürk Orman Çiftliği'],
        #'İzmir': ['Konak Meydanı', 'Asansör', 'Kemeraltı Çarşısı'],
        #'Bursa': ['Ulu Camii', 'Uludağ', 'Tophane Saat Kulesi'],
        #'Antalya': ['Kaleiçi', 'Düden Şelalesi', 'Perge Antik Kenti']


    #if selected_city in tourist_spots:
        #selected_spot = st.selectbox('Turistik Yer Seçin', tourist_spots[selected_city])
        #st.write('Seçilen turistik yer:', selected_spot)
    #else:
        #st.write('Bu şehre ait turistik yerler bulunmamaktadır.')
    selected_city = st.button("Yer Seç")

    if selected_city:
        prompt = f"""
        You are a tour guide who is an expert on history, antiquity and natural beauties. 
        Tell him about {selected_spots} as if you were telling a story, adhering to facts.
        Output must be in Turkish, other languages are not acceptable.
        
        """

        response, prompt_token_count, response_token_count = get_gemini_response(prompt)
        #st.markdown(response.text)

