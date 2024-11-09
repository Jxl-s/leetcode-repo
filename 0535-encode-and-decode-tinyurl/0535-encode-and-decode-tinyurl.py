urls = {}
counter = 0

class Codec:

    def encode(self, longUrl: str) -> str:
        global counter
        """Encodes a URL to a shortened URL.
        """
        encoded = str(counter)

        urls[encoded] = longUrl
        counter += 1

        return encoded

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return urls[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))