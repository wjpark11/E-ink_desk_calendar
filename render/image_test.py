import calendar
from datetime import date, timedelta
from PIL import Image, ImageDraw, ImageFont

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 480
TICK = 10

base_img = Image.new("1", (DISPLAY_WIDTH, DISPLAY_HEIGHT), color=1)
draw = ImageDraw.Draw(base_img)
draw.point(
    [
        (x, y)
        for x in range(0, DISPLAY_WIDTH, TICK)
        for y in range(0, DISPLAY_HEIGHT, TICK)
    ],
    fill=0,
)

calendar_year = 2015
calendar_month = 4

year_of_next_month = calendar_year if calendar_month < 12 else calendar_year + 1
next_month = calendar_month + 1 if calendar_month < 12 else 1

year_of_prev_month = calendar_year if calendar_month > 1 else calendar_year - 1
prev_month = calendar_month - 1 if calendar_month > 1 else 12

mini_cal_font = ImageFont.truetype("./font/D2Coding.ttf", 8)
calendar_day_font = ImageFont.truetype("./font/D2Coding.ttf", 14)

month_calendar = calendar.Calendar().monthdayscalendar(calendar_year, calendar_month)
calendar_width = 530
calendar_height = 390
calendar_line_num = len(month_calendar)
calendar_cell_width = int(490 / 7)
calendar_cell_height = int(360 / calendar_line_num)
calendar_cell_padding = 3
weeknum_cell_width = 40
weekname_cell_height = 30
calendar_position_x, calendar_position_y = 0, 90

cell_date_positions = [
    [
        [
            calendar_position_x
            + weeknum_cell_width
            + i * calendar_cell_width
            + calendar_cell_padding,
            calendar_position_y
            + weekname_cell_height
            + j * calendar_cell_height
            + calendar_cell_padding,
        ]
        for i in range(7)
    ]
    for j in range(calendar_line_num)
]

cal = calendar.TextCalendar()
prev_cal = cal.formatmonth(year_of_prev_month, prev_month)
next_cal = cal.formatmonth(year_of_next_month, next_month)


draw.text((2, 2), prev_cal, font=mini_cal_font, fill=0)
draw.text((450, 2), next_cal, font=mini_cal_font, fill=0)

# calendar outline
draw.rectangle(
    (
        calendar_position_x,
        calendar_position_y,
        calendar_position_x + calendar_width,
        calendar_position_y + calendar_height,
    ),
    fill=1,
    outline=0,
)

# weeknum right line
draw.line(
    (
        calendar_position_x + weeknum_cell_width,
        calendar_position_y,
        calendar_position_x + weeknum_cell_width,
        calendar_position_y + calendar_height,
    ),
    fill=0,
    width=2,
)

# weekday name bottom line
draw.line(
    (
        calendar_position_x,
        calendar_position_y + weekname_cell_height,
        calendar_position_x + calendar_width,
        calendar_position_y + weekname_cell_height,
    ),
    fill=0,
    width=2,
)

# calendar cell vertical lines
for i in range(0, calendar_width - weeknum_cell_width, calendar_cell_width):
    draw.line(
        (
            calendar_position_x + weeknum_cell_width + i,
            calendar_position_y,
            calendar_position_x + weeknum_cell_width + i,
            calendar_position_y + calendar_height,
        ),
        fill=0,
        width=1,
    )

# calendar cell horizontal lines
for i in range(0, calendar_height - weekname_cell_height, calendar_cell_height):
    draw.line((0, 90 + 30 + i, 530, 90 + 30 + i), fill=0, width=1)

# calendar cell date
for i in range(calendar_line_num):
    for j in range(7):
        if month_calendar[i][j] != 0:
            draw.text(
                cell_date_positions[i][j],
                str(month_calendar[i][j]),
                font=calendar_day_font,
                fill=0,
            )


base_img.show()
