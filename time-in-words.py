# Right Solution


def timeInWords(h, m):
    # Write your code here
    minutes_to_word = {1: 'one', 2: 'two', 3: 'three', 4: 'four',
                       5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve'}
    position_minutes_to_word = {2: "twen", 3: 'thir', 4: 'fourth',
                                5: 'fifth', 6: 'sixth', 7: 'seventh', 8: 'eigh', 9: 'nine'}

    if m == 0:
        return f"{minutes_to_word[h]} o' clock"
    elif m == 1 or 60-m == 1:
        return f"{minutes_to_word[60-m if m>30 else m]} minute {'to' if m>30 else 'past'} {minutes_to_word[h+1 if m>30 else h]}"
    elif 1 < m <= 10 or 1 <= 60-m <= 10:
        return f"{minutes_to_word[60-m if m>30 else m]} minutes {'to' if m>30 else 'past'} {minutes_to_word[h+1 if m>30 else h]}"
    elif 10 < m <= 12 or 10 < 60-m <= 12:
        return f"{minutes_to_word[(60-m) if m>30 else m]} minutes {'to' if m>30 else 'past'} {minutes_to_word[h+1 if m>30 else h]}"
    elif (12 <= m <= 14 or 15 < m <= 19) or (12 <= 60-m <= 14 or 15 < 60-m <= 19):
        return f"{position_minutes_to_word[(60-m)%10 if m>30 else m%10]}teen minutes {'to' if m>30 else 'past'} {minutes_to_word[h+1 if m>30 else h]}"
    elif m == 15 or m == 45:
        return f"quarter {'to' if m==45 else 'past'} {minutes_to_word[h+1 if m==45 else h]}"
    elif m == 20:
        return f"twenty minutes past {minutes_to_word[h]}"
    elif (21 <= m <= 29) or (21 <= 60-m <= 29):
        return f"twenty {minutes_to_word[(60-m)%10 if m>30 else m%10]} minutes {'to' if m>30 else 'past'} {minutes_to_word[h+1 if m>30 else h]}"
    elif m == 30:
        return f"half past {minutes_to_word[h]}"


print(timeInWords(1, 1))
print(timeInWords(5, 10))
print(timeInWords(5, 12))
print(timeInWords(5, 13))
print(timeInWords(5, 15))
print(timeInWords(5, 17))
print(timeInWords(5, 20))
print(timeInWords(5, 23))
print(timeInWords(7, 29))
print(timeInWords(5, 30))
print(timeInWords(5, 32))
print(timeInWords(5, 42))
print(timeInWords(5, 45))
print(timeInWords(5, 47))
print(timeInWords(5, 50))
print(timeInWords(5, 52))
