"""A video player class."""

from .video_library import VideoLibrary
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.current_video = None
        self.pause = False
       

    def number_of_videos(self):
        """Returns the number of videos"""
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")


    def show_all_videos(self):
        """Returns all videos."""
        videos1 = self._video_library.get_all_videos()
        videos = sorted(videos1, key=lambda x: x.title)

        print("Here's a list of all available videos:")
        for video in videos:
            if video.tags:
                print(f"{video.title} ({video.video_id}) [{video.tags[0]} {video.tags[1]}]")
            else:
                print(f"{video.title} ({video.video_id}) []")
        
        
        

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        
        if self.current_video == None:
            if self._video_library.get_video(video_id) == None:
                print("Cannot play video: Video does not exist")
            else:
                video = self._video_library.get_video(video_id)
                print(f"Playing video: {video.title}")
                self.current_video_id = video.video_id
                self.current_video = video
                self.pause = False

        else:
            video = self._video_library.get_video(video_id)
            if video == None:
                print("Cannot play video: Video does not exist")
            else:
                self.stop_video()
                print(f"Playing video: {video.title}")
                self.current_video_id = video.video_id
                self.current_video = video
                self.pause = False
        
       
    def stop_video(self):
        """Stops the current video."""
        if self.current_video == None:
            print(f"Cannot stop video: No video is currently playing")
        else:   
            print(f"Stopping video: {self.current_video.title}")
            self.current_video = None


    def play_random_video(self):
        """Plays a random video from the video library."""
        videos = self._video_library.get_all_videos()
        video_ids = []
        for video in videos:
            video_ids.append(video.video_id)

        id = random.choice(video_ids)
        self.play_video(id)



    def pause_video(self):
        """Pauses the current video."""
        if self.current_video == None:
            print(f"Cannot pause video: No video is currently playing")
        else:
            if self.pause == True:
                print(f"Video already paused: {self.current_video.title}")
            else:
                print(f"Pausing video: {self.current_video.title}")
                self.pause = True
                

    def continue_video(self):
        """Resumes playing the current video."""
        if self.current_video == None:
            print(f"Cannot continue video: No video is currently playing")
        elif self.pause == False:
            print(f"Cannot continue video: Video is not paused")

        else:
            self.pause = False
            print(f"Continuing video: {self.current_video.title}")


    def show_playing(self):
        """Displays video currently playing."""
        if self.current_video == None:
            print(f"No video is currently playing")

        else:
            paused = ""
            if self.pause == True:
                paused = "- PAUSED"
            if self.current_video.tags:
                print(f"Currently playing: {self.current_video.title} ({self.current_video.video_id}) [{self.current_video.tags[0]} {self.current_video.tags[1]}] {paused}")
            else:
                print(f"Currently playing: {self.current_video.title} ({self.current_video.video_id}) [] {paused}")


    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
