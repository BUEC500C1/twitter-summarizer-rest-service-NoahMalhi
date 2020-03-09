import main
import dev_image
import twitter_fetch
import pytest

#just tests successfull run
testname = "testname"
def test_twitterpull():
    (tweet_texts , image_list) = main.main(testname)
    actual = ["This is a pytest test tweet", "Seconds test tweet", "Thirdd, no image"]
    assert all([a==b for a,b in zip(actual, tweet_texts)])

    assert main.main("123") == 0
    assert main.main("") == 0
    