from kivy.uix.widget import Widget

class Grid(Widget):
    def __init__(self, **kwargs):
        super(Grid, self).__init__(**kwargs)        
        self.register_event_type('on_select')        
        self.cols = 0
        self.rows = 0
        self.selected = (0,0)
        self.selected_range = []
        self.bg_color = '#FFFFFF'
        self.text_color = '#000000'
    def make(self, rows=0, cols=0, template=None):
        for row in range(rows):
            self.add_row
            for col in range(cols):
                #add cell (row, col)
    def reset(self):
        '''eliminate all rows, cols, contents, styles'''
        
    def clear(self):
        '''remove all cell and label values'''
        pass
    #grid setup/teardown
    def add_row(self, label=None, num=1, loc=self.rows):
        '''self.add_row(): insert one row at the bottom of the grid'''
        self.rows += num
    def add_col(self, label=None, num=1, loc=self.cols):
        '''self.add_col(): insert one column at the right of the grid'''
        self.cols += num
    def set_row_label_value(self, row, label):
        pass
    def get_row_label_value(self, row):
        pass
    def set_col_label_value(self, col, label):
        pass
    def get_col_label_value(self, col):
        pass    
    def del_row(self, row=self.rows):
        pass
    def del_col(self, col):
        pass
    def hide_row(self, row):
        pass
    def hide_col(self, col):
        pass
    def set_cell(self, row, col):
        pass
    def get_cell(self, row, col):
        pass  
    
    #interaction
    def sort(self, col):
        pass
    def filter(self, col, value):
        pass
    def get_selection(self):
        pass
    def set_selection(self, cell):
        pass
    def can_edit(self, edit=True):
        pass
    def can_edit_cell(self, cell, edit=True):
        pass
    
    #sizing
    def autosize(self, height=True, width=True):
        pass
    def autosize_rows(self, height=True, width=True):
        pass
    def autosize_cols(self, height=True, width=True):
        pass    
    def autosize_row_labels(self, height=True, width=True):
        pass    
    def autosize_col_labels(self, height=True, width=True):
        pass    
    def set_size(self, x, y):
        pass
    def get_size(self):
        pass
    def set_col_size(self, col):
        pass
    def set_row_size(self row):
        pass
    def can_resize(self):
        pass
    def can_resize_rows(self):
        pass
    def can_resize_cols(self):
        pass
    
    #styles
    def set_bg(self, background):
        '''takes color (graphics too?) and makes it the grid background'''
        pass
    def set_cell_bg(self, background):
        pass
    def style_text(self, color='#000000', font='', style='default'):
        pass
    def style_labels(self, text_color='#000000', font='', bg_color=self.bg_color, 
                     border_width=1, border_color='#000000', border_type='solid'):
        pass
    def style_grid(self, cell_padding=3, line_width=1, line_type='solid', line_color='#000000'):
        '''all overall style settings should be possible to set through this shortcut method'''
        pass
    def style_border(self, width=1, type='solid', color='#000000'):
        pass
    def set_cell_padding(self, top, bottom, left, right, cell=None):
        pass
    def set_line_width(self, width):
        pass
    def set_line_type(self, type):
        pass
    def set_line_color(self, color):
        pass

    #event-related
    def select(self, data):
        '''Call this method to trigger the `on_select` event, with the `data`
        selection. The `data` can be anything you want.
        '''
        self.dispatch('on_select', data)
        if self.dismiss_on_select:
            self.dismiss()    