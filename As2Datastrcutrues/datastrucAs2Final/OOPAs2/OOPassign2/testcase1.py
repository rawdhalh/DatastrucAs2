from classes import * 
def test_add_artwork():
    # Create a museum
    louvre = Museum("Louvre", "Abu Dhabi")

    # Create artworks
    mona_lisa = Artwork("Mona Lisa", "Leonardo da Vinci", "1503", "Renaissance Painting")
    starry_night = Artwork("Starry Night", "Vincent van Gogh", "1889", "Post-Impressionist ")

    # Add artworks to the museum
    louvre.add_artwork(mona_lisa)
    louvre.add_artwork(starry_night)


    # Print the added artworks
    print("Artworks added to the museum:")
    for artwork in louvre.get_artworks():
        print(artwork.get_title())

if __name__ == "__main__":
    test_add_artwork()

