import requests
from lxml import html
import streamlit as st
from groq import Groq
import os
from deep_translator import GoogleTranslator
import math

def parse_groq_stream(stream):
    for chunk in stream:
        if chunk.choices:
            if chunk.choices[0].delta.content is not None:
                yield chunk.choices[0].delta.content

try:
    # secrets = dotenv_values(".env")  # for dev env
    GROQ_API_KEY = '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'
except:
    secrets = st.secrets  # for streamlit deployment
    GROQ_API_KEY = secrets["GROQ_API_KEY"]

# save the api_key to environment variable
os.environ["GROQ_API_KEY"] = GROQ_API_KEY


client = Groq()

#GCC Scraping
def al_bayan(url):
    try:
        # Fetch the page content
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP issues

        # Parse the HTML content
        tree = html.fromstring(response.content)

        # Extract the title
        title_element = tree.xpath('//h1')
        title_text = title_element[0].text_content().strip() if title_element else "Title not found"

        # Extract the date
        date_element = tree.xpath('//time[@class="post-time"]')
        date_text = date_element[0].text_content().strip() if date_element else "Date not found"

        # Extract the article content
        paragraph_divs = tree.xpath('//p[@class="article-text"]')
        content = "\n".join([p.text_content().strip() for p in paragraph_divs]) if paragraph_divs else "Content not found"

        # Return the extracted details as a dictionary
        return {
            "title": title_text,
            "date": date_text,
            "content": content
        }

    except requests.RequestException as e:
        return {"error": f"Failed to fetch the URL: {e}"}

    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}


def al_bayan(url):
    try:
        # Fetch the page content
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP issues

        # Parse the HTML content
        tree = html.fromstring(response.content)

        # Extract the title
        title_element = tree.xpath('//h1')
        title_text = title_element[0].text_content().strip() if title_element else "Title not found"

        # Extract the date
        date_element = tree.xpath('//div[@class="art-date"]')
        date_text = date_element[0].text_content().strip() if date_element else "Date not found"

        # Extract the article content
        paragraph_divs = tree.xpath('//p[@style="text-align: justify;"]')
        content = "\n".join([p.text_content().strip() for p in paragraph_divs]) if paragraph_divs else "Content not found"

        # Return the extracted details as a dictionary
        return {
            "title": title_text,
            "date": date_text,
            "content": content
        }

    except requests.RequestException as e:
        return {"error": f"Failed to fetch the URL: {e}"}

    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}


def aletihad(url):
    # Extract details from Aletihad articles
    try:
        response = requests.get(url)
        response.raise_for_status()
        tree = html.fromstring(response.content)

        title_element = tree.xpath('//h1')
        title_text = title_element[0].text_content().strip() if title_element else "Title not found"

        date_element = tree.xpath('//div[@class="art-date"]')
        date_text = date_element[0].text_content().strip() if date_element else "Date not found"

        paragraph_divs = tree.xpath('//p[@style="text-align: justify;"]')
        content = "\n".join([p.text_content().strip() for p in paragraph_divs]) if paragraph_divs else "Content not found"

        return {"title": title_text, "date": date_text, "content": content}

    except requests.RequestException as e:
        return {"error": f"Failed to fetch the URL: {e}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"} 


def gulf_news(url):
    try:
        # Fetch the page content
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP issues

        # Parse the HTML content
        tree = html.fromstring(response.content)

        # Extract the title
        title_element = tree.xpath('//h1')
        title_text = title_element[0].text_content().strip() if title_element else "Title not found"

        # Extract the date
        date_element = tree.xpath('//time[@class="publish"]')
        date_text = date_element[0].text_content().strip() if date_element else "Date not found"

        # Extract the article content
        paragraph_divs = tree.xpath('//div[@class="article-body"]')
        content = "\n".join([p.text_content().strip() for p in paragraph_divs]) if paragraph_divs else "Content not found"

        # Return the extracted details as a dictionary
        return {
            "title": title_text,
            "date": date_text,
            "content": content
        }

    except requests.RequestException as e:
        return {"error": f"Failed to fetch the URL: {e}"}

    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}




def emarat_alyoum(url):
    try:
        # Fetch the page content
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP issues

        # Parse the HTML content
        tree = html.fromstring(response.content)

        # Extract the title
        title_element = tree.xpath('//h1')
        title_text = title_element[0].text_content().strip() if title_element else "Title not found"

        # Extract the date
        date_element = tree.xpath('//time[@class="date"]')
        date_text = date_element[0].text_content().strip() if date_element else "Date not found"

        # Extract the article content
        paragraph_divs = tree.xpath('//div[@class="col"]')
        content = "\n".join([p.text_content().strip() for p in paragraph_divs]) if paragraph_divs else "Content not found"

        # Return the extracted details as a dictionary
        return {
            "title": title_text,
            "date": date_text,
            "content": content
        }

    except requests.RequestException as e:
        return {"error": f"Failed to fetch the URL: {e}"}

    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}

def cnn_arabic(url):
    try:
        # Fetch the page content
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP issues

        # Parse the HTML content
        tree = html.fromstring(response.content)

        # Extract the title
        title_element = tree.xpath('//h1')
        title_text = title_element[0].text_content().strip() if title_element else "Title not found"

        # Extract the date
        date_element = tree.xpath('//time')
        date_text = date_element[0].attrib.get('datetime') if date_element else "Date not found"

        # Extract the article content
        paragraph_divs = tree.xpath('//div[@id="body-text"]')
        content = "\n".join([p.text_content().strip() for p in paragraph_divs]) if paragraph_divs else "Content not found"

        # Return the extracted details as a dictionary
        return {
            "title": title_text,
            "date": date_text,
            "content": content
        }

    except requests.RequestException as e:
        return {"error": f"Failed to fetch the URL: {e}"}

    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}



def masaader(url):
    try:
        # Fetch the page content
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP issues

        # Parse the HTML content
        tree = html.fromstring(response.content)

        # Extract the title
        title_element = tree.xpath('//h1')
        title_text = title_element[0].text_content().strip() if title_element else "Title not found"

        # Extract the date
        date_element = tree.xpath('//abbr[@class="date published"]')
        date_text = date_element[0].text_content().strip() if date_element else "Date not found"

        # Extract the article content
        paragraph_divs = tree.xpath('//div[@class="entry-content clearfix"]')
        content = "\n".join([p.text_content().strip() for p in paragraph_divs]) if paragraph_divs else "Content not found"

        # Return the extracted details as a dictionary
        return {
            "title": title_text,
            "date": date_text,
            "content": content
        }

    except requests.RequestException as e:
        return {"error": f"Failed to fetch the URL: {e}"}

    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}



def site_selector(url):
    if "www.albayan.ae" in url:
        return al_bayan(url)
    elif "www.aletihad.ae" in url:
        return aletihad(url)
    elif "gulfnews.com" in url:
        return gulf_news(url)
    elif "www.emaratalyoum.com" in url:
        return emarat_alyoum(url)
    elif "arabic.cnn.com" in url:
        return cnn_arabic(url)
    elif "masaadernews.com" in url:
        return masaader(url)
    else:
        print("We are working on pther URLs please be paitent.")



def lang_trans(data):
    if data is None or (isinstance(data, float) and math.isnan(data)):
        return data  # Pass None and NaN values without translation
    
    # Ensure data is a string
    if not isinstance(data, str):
        return data  # Pass non-string values without translation

    # Translate to English
    try:
        english_translation = GoogleTranslator(source='auto', target='en').translate(data)
    except Exception as e:
        print(f"Translation failed for data: {data}, error: {e}")
        return data  # Return original data if translation fails
    
    return english_translation

def translate_article_data(article_data):
    """
    Translates the article data (title, date, content) to English
    """
    if not isinstance(article_data, dict):
        return article_data
    
    translated_data = {}
    for key, value in article_data.items():
        if key in ['title', 'content']:
            translated_data[key] = lang_trans(value)
        else:
            translated_data[key] = value
    
    return translated_data




# Streamlit App
st.set_page_config(
    page_title="News Summarization and Sentiment Analysis",
    page_icon="🤖",
    layout="centered",
)

st.title("News App")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "assistant", 
         "content": "Hi. Paste your news article link for summary and sentiment classification."}
    ]

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"], avatar='🤖' if message["role"] == "assistant" else "🗨️"):
        st.markdown(message["content"])

# URL input using chat_input
url = st.chat_input("Enter the article URL here")

# Process URL when submitted
# Process URL when submitted
if url:
    # Get the article content
    result = site_selector(url)
    
    if "error" in result:
        st.error(result["error"])
    else:
        # Translate the content
        translated_result = translate_article_data(result)
        
        # Display the translated content
        with st.chat_message("user", avatar="🗨️"):
            st.markdown("**Original Title:**")
            st.markdown(result['title'])
            st.markdown("**Translated Title:**")
            st.markdown(translated_result['title'])
            st.markdown("**Publication Date:**")
            st.markdown(translated_result['date'])
            st.markdown("**Translated Content:**")
            st.markdown(translated_result['content'])
        
        # Add translated content to chat history
        st.session_state.chat_history.append(
            {"role": "user", "content": translated_result['content']})
        
        # Process with Groq
        messages = [
            {"role": "system", "content": '''You are an AI assistant specializing in news analysis of Saudi Aramco. 
            Please provide:
            1. A concise summary of the article
            2. The main sentiment (positive, negative, or neutral)
            3. Key points and implications'''},
            {"role": "assistant", "content": ""},
            *st.session_state.chat_history
        ]
        
        # Display assistant response
        with st.chat_message("assistant", avatar='🤖'):
            try:
                stream = client.chat.completions.create(
                    model="llama-3.2-3b-preview",
                    messages=messages,
                    stream=True
                )
                response = st.write_stream(parse_groq_stream(stream))
                st.session_state.chat_history.append(
                    {"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"Error processing with AI: {str(e)}")
