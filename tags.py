

class MifareClassic1k:
    def __init__(self, uid, atqa, sak, blocks, sector_keys, date, files):
        self.uid = uid
        self.atqa = atqa
        self.sak = sak
        self.blocks = blocks
        self.sector_keys = sector_keys
        self.date = date
        self.files = files

    def __str__(self):
        formatted_date = self.date.strftime("%d-%m-%Y %H:%M:%S")
        return f"    Date: {formatted_date}\n    UID: {self.uid}"

    def get_basic_info(self):
        card = f"UID: {self.uid}\nATQA: {self.atqa}\nSAK: {self.atqa}\n"
        line = " ---------------------------------------"
        memory = f"\nMemory:\n{line}\n"
        for n in range(64):
            memory += f"| {str(n).rjust(2, ' ')} | {self.blocks[str(n)]} |\n"
            if (n+1)%4 == 0:
                memory += f"{line}\n"
        text = card + memory
        return text
