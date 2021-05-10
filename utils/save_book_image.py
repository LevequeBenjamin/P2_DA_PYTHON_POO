

def save_book_image(self, soup, book_informations, category):
        try:
            response = requests.get(book_informations["image_url"], stream=True)
            if response.status_code == 200:
                dir_path = f"data/{category}/images"
                filename = book_informations["image_filename"]
                if not os.path.exists(dir_path):
                    os.makedirs(f"data/{category}/images")
                file_path = os.path.join(dir_path, filename)
                response.raw.decode_content = True
                with open(f"{file_path}", "wb") as file:
                    shutil.copyfileobj(response.raw, file)
            elif not response.status_code // 100 == 2:
                print(f"Error: Unexpected response {response}")
        except requests.exceptions.RequestException as error:
            print(f"Error: {error}")
            

#urllib.request.urlretrieve(image_url, 'downloads/images/' + filename)