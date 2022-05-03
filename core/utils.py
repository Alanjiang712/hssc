from core.signals import operand_started, operand_finished
class SendSignalsMixin:
    def send_operand_finished(self, pid):
        # 构造作业完成消息参数
        ocode = 'RTC'
        form_data=self.request.POST.copy()
        form_data.pop('csrfmiddlewaretoken')
        operand_finished.send(sender=self, pid=pid, ocode=ocode, uid=self.request.user, form_data=form_data)

    def send_operand_started(self, pid):
        ocode = 'RTR'
        operand_started.send(sender=self, pid=pid, ocode=ocode, uid=self.request.user)


def keyword_replace(s, replace_dict):
    '''
    keyword_replace
    '''
    import re
    next = []
    changed_str = s

    def buildNext():
        next.append(0)
        x = 1
        now = 0
        while x < len(p):
            if p[now] == p[x]:
                now += 1
                x += 1
                next.append(now)
            elif now:
                now = next[now-1]
            else:
                next.append(0)
                x += 1

    def search(new_str):
        tar = 0
        pos = 0
        while tar < len(s):
            if s[tar] == p[pos]:
                tar += 1
                pos += 1
            elif pos:
                pos = next[pos-1]
            else:
                tar += 1
            if pos == len(p):   # 匹配成功
                next_str = re.sub(p, replace_dict[p], new_str)
                pos = next[pos-1]
                return next_str

    for p in replace_dict:
        buildNext()
        changed_str = search(changed_str)

    return changed_str


def keyword_search(s, keywords_list):
    '''
    keyword_search
    '''
    next = []
    match = []

    def buildNext():
        next.append(0)
        x = 1
        now = 0
        while x < len(p):
            if p[now] == p[x]:
                now += 1
                x += 1
                next.append(now)
            elif now:
                now = next[now-1]
            else:
                next.append(0)
                x += 1

    def search():
        tar = 0
        pos = 0
        while tar < len(s):
            if s[tar] == p[pos]:
                tar += 1
                pos += 1
            elif pos:
                pos = next[pos-1]
            else:
                tar += 1
            if pos == len(p):   # 匹配成功
                match.append(p)
                pos = next[pos-1]

    for p in keywords_list:
        buildNext()
        search()
    keywords = sorted(set(match), key=match.index)
    return keywords
