import globals


class Score:
    def __init__(self):
        """set the number of points.
        Args:
            self (Score):  an instance of the class.
        Returns:
            None
        """
        self.points = 0
        self.record = 0

    def read_record(self):
        """reads the record from the file.
        Args:
            self (Score):  an instance of the class.
        Returns:
            int: the current game record.
        """
        my_file = open("records.txt", 'r')
        cur_record = int(my_file.readline())
        my_file.close()
        return cur_record

    def draw_score(self):
        """reflects the score instance on the screen.
        Args:
            self (Score):  an instance of the class.
        Returns:
            None.
        """
        score_text = globals.font_style.render(f'Score: {self.points}',
                                               True, globals.BLUE)
        record_text = globals.font_style.render(f'Your record: {self.record}',
                                               True, globals.BLUE)
        cur_record = self.read_record()
        if self.points > cur_record:
            my_file = open("records.txt", 'w')
            my_file.write(str(self.points))
            my_file.close()
        score_tablet = score_text.get_rect()
        record_tablet = record_text.get_rect()
        score_tablet.topleft = (5, 5)
        record_tablet.topleft = (5, 30)
        globals.DISPLAY_SURFACE.blit(score_text, score_tablet)
        globals.DISPLAY_SURFACE.blit(record_text, record_tablet)