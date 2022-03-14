def solution(participant, completion):

    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i] : return participant[i]
        return participant[i]



participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
comletion = ["josipa", "filipa", "marina", "nikola"]
solution(participant, comletion)