def solution(video_len, pos, op_start, op_end, commands):
    start=(int(op_start[3:])) + (int(op_start[:2]) * 60)
    end=(int(op_end[3:])) + (int(op_end[:2]) * 60)
    real_pos=(int(pos[3:])) + (int(pos[:2]) * 60)
    video=(int(video_len[3:])) + (int(video_len[:2]) * 60)
    mm = 0
    ss = 0
    if start <= real_pos <= end:
        real_pos = end

    for i in commands:
        if start <= real_pos <= end:
            real_pos = end
        if i == "next":
            real_pos += 10
            if real_pos > video:
                real_pos = video
            if start <= real_pos <= end:
                real_pos = end      
        else:
            real_pos -= 10
            if real_pos <= 0:
                real_pos = 0
            elif start <= real_pos <= end:
                real_pos = end
    if real_pos > video:
        return video_len
        
    mm += int(real_pos / 60)
    ss += int(real_pos % 60)
        
    if real_pos < 60:
        if real_pos == 0:
            return f"00:00"
        else:
            if ss < 10:
                return f"00:0{ss}"
            else:
                return f"00:{ss}"
    else:
        if mm < 10:
            if ss < 10:
                return f"0{mm}:0{ss}"
            else:
                return f"0{mm}:{ss}"
        else:
            if ss < 10:
                return f"{mm}:0{ss}"
            else:
                return f"{mm}:{ss}"