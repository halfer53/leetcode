class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9+7
        @cache
        def dp(unique_songs, listened_songs):
            if unique_songs == 0 and listened_songs==0:return 1
            if unique_songs<0 or unique_songs>listened_songs:return 0
            res = dp(unique_songs-1, listened_songs-1)*(n-(unique_songs-1))  % MOD
            if unique_songs-k > 0:
                res += dp(unique_songs, listened_songs-1)*(unique_songs-k) % MOD
            return res % MOD
        return dp(n, goal)