#Thư viện PyTeX.py hỗ trợ soạn thảo tài liệu bằng gói ex_test.sty trong LaTeX
#Liên hệ: Nguyễn Hoàng Hải (hoanghai@hcmut.edu.vn), Hoàng Trọng Tấn (httandayonline@gmail.com)
#############################################################################
import re
from collections import defaultdict

class QuestionBank:
    def __init__(self):
        self.questions_by_id = {}
        self.questions_by_type = defaultdict(list)
        self.questions_by_info = defaultdict(list)
        self.questions_by_begin = defaultdict(list)

    def add_question(self, question_data):
        question_id = question_data.get('id')
        if question_id:
            self.questions_by_id[question_id] = question_data
        self.questions_by_type[question_data['type']].append(question_data)
        if question_data.get('info'):
            self.questions_by_info[question_data['info']].append(question_data)
        if question_data.get('begin'):
            self.questions_by_begin[question_data['begin']].append(question_data)

    def find_by_id(self, search_term, use_regex=True):
        if "[" not in search_term and "." not in search_term:
            use_regex = False

        if use_regex:
            pattern = re.compile(search_term)
            return [q for q in self.questions_by_id.values() if pattern.match(q['id'])]
        else:
            question = self.questions_by_id.get(search_term)
            return [question] if question else []

    def find_by_type(self, question_type):
        return self.questions_by_type[question_type]

    def find_by_info(self, question_info):
        return self.questions_by_info[question_info]

    def find_by_begin(self, question_begin):
        return self.questions_by_begin[question_begin]

def get_bank(tex_content):
    question_patterns = r'\\begin\{ex\}.*?\\end\{ex\}|\\begin\{bt\}.*?\\end\{bt\}|\\begin\{vd\}.*?\\end\{vd\}'
    questions = re.findall(question_patterns, tex_content, re.DOTALL)

    question_bank = QuestionBank()

    for question_text in questions:
        all_info = re.findall(r'%\[(.*?)\]', question_text)
        question_id = next((info for info in all_info if re.match(r'^\S{5,8}$', info)), None)
        question_info = next((info for info in all_info if not re.match(r'^\S{5,8}$', info)), None)

        question_type = 'longans'
        if '\\shortans' in question_text:
            question_type = 'shortans'
        elif '\\choiceTF' in question_text:
            question_type = 'choiceTF'
        elif '\\choice' in question_text:
            question_type = 'choice'

        question_begin_match = re.search(r'\\begin\{(ex|bt|vd)\}', question_text)
        question_begin = question_begin_match.group(1) if question_begin_match else None

        question_data = {
            'id': question_id,
            'type': question_type,
            'info': question_info,
            'begin': question_begin,
            'content': question_text
        }

        question_bank.add_question(question_data)

    return question_bank
