# 장르 별로 가장 많이 재생된 노래 두개씩 모음.
def solution(genres, plays):
    play_cnt = {}
    music = {}
    num = 0
    for genre, play in zip(genres, plays):
        if genre not in play_cnt.keys():
            play_cnt[genre] = play
        else:
            play_cnt[genre] += play

        if genre not in music.keys():
            music[genre] = [[play, num]]
        else:
            music[genre].append([play, num])

        num += 1

    # 음악 재생횟수가 큰 순서대로 정렬
    for i in music.keys():
        music[i] = sorted(music[i], key=lambda x: (-x[0], x[1]))

    seq = []
    # 장르의 순서 먼저 정하기
    for i in play_cnt.keys():
        seq.append([play_cnt[i], i])

    seq = sorted(seq, key=lambda x: (-x[0]))
    # print(seq)
    # print(music)

    ans = []
    for i in seq:
        i = i[1]
        if len(music[i]) < 2:
            ans.append(music[i][0][1])
        else:
            tmp = music[i][:2]
            for i in tmp:
                ans.append(i[1])

    return ans