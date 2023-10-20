def solution(genres, plays):
    genre_play_count = {}
    genre_songs = {}
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        
        if genre in genre_play_count:
            genre_play_count[genre] += play
            genre_songs[genre].append((i, play))
        else:
            genre_play_count[genre] = play
            genre_songs[genre] = [(i, play)]
    
    sorted_genres = sorted(genre_play_count.keys(), key=lambda x: genre_play_count[x], reverse=True)
    answer = []
    
    for genre in sorted_genres:
        songs = genre_songs[genre]
        songs.sort(key=lambda x: (-x[1], x[0]))
        answer.extend([song[0] for song in songs[:2]])
    
    return answer
