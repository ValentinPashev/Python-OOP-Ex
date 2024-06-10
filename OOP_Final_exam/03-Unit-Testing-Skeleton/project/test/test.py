from unittest import TestCase, main

from project import SocialMedia


class TestSocialMedia(TestCase):

    def setUp(self):
        self.social_media = SocialMedia("test_user", "Instagram", 1000, "photo")

    def test_create_post(self):
        self.assertEqual(self.social_media.create_post("Test post"), "New photo post created by test_user on Instagram.")
        self.assertEqual(len(self.social_media._posts), 1)

    def test_like_post(self):
        self.social_media.create_post("Test post")
        for _ in range(10):  # Updated this line
            self.assertEqual(self.social_media.like_post(0), "Post liked by test_user" if _ < 9 else "Post has reached the maximum number of likes.")  # Updated this line
        self.assertEqual(self.social_media.like_post(1), "Invalid post index.")

    def test_comment_on_post(self):
        self.social_media.create_post("Test post")
        self.assertEqual(self.social_media.comment_on_post(0, "Nice post!"), "Comment added by test_user on the post")
        self.assertEqual(self.social_media.comment_on_post(0, "Short"), "Comment should be more than 10 characters.")

    def test_platform_property(self):
        self.assertEqual(self.social_media.platform, "Instagram")
        self.social_media.platform = "YouTube"
        self.assertEqual(self.social_media.platform, "YouTube")
        with self.assertRaises(ValueError):
            self.social_media.platform = "InvalidPlatform"

    def test_followers_property(self):
        self.assertEqual(self.social_media.followers, 1000)
        self.social_media.followers = 2000
        self.assertEqual(self.social_media.followers, 2000)
        with self.assertRaises(ValueError):
            self.social_media.followers = -100

    def test_invalid_post_index(self):
        self.assertEqual(self.social_media.like_post(-1), "Invalid post index.")
        self.assertEqual(self.social_media.like_post(100), "Invalid post index.")

    def test_comment_length(self):
        self.social_media.create_post("Test post")
        self.assertEqual(self.social_media.comment_on_post(0, "Short"), "Comment should be more than 10 characters.")
        self.assertEqual(self.social_media.comment_on_post(0, "This is a long comment!"), "Comment added by test_user on the post")

    def test_invalid_platform(self):
        with self.assertRaises(ValueError):
            SocialMedia("test_user", "InvalidPlatform", 1000, "photo")

    # Additional negative test cases
    def test_negative_followers(self):
        with self.assertRaises(ValueError):
            self.social_media.followers = -500

    def test_invalid_comment_length(self):
        self.social_media.create_post("Test post")
        self.assertEqual(self.social_media.comment_on_post(0, "Short"), "Comment should be more than 10 characters.")
        self.assertEqual(self.social_media.comment_on_post(0, "Too short!"), "Comment should be more than 10 characters.")

    def test_invalid_post_creation(self):
        with self.assertRaises(ValueError):
            self.social_media.create_post("")

    def test_invalid_like_post_index(self):
        self.assertEqual(self.social_media.like_post(5), "Invalid post index.")

if __name__ == '__main__':
    main()