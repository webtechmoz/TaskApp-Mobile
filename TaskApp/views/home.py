import flet as ft

def home(page: ft.Page, width: int, height: int):

    textcolor = ft.colors.with_opacity(0.6, 'white')

    def criar_tarefa(e: ft.ControlEvent):
        if task_textfield.value != '':
            tarefas_criadas.controls.append(
                ft.Container(
                    border=ft.border.all(
                        width=1,
                        color=textcolor
                    ),
                    height=50,
                    padding=ft.padding.only(
                        left=8,
                        right=5
                    ),
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                value=task_textfield.value,
                                color=textcolor,
                                size=14,
                                weight='bold'
                            ),
                            ft.Row(
                                controls=[
                                    ft.IconButton(
                                        icon=ft.icons.EDIT,
                                        icon_color=ft.colors.BLUE,
                                        icon_size=20,
                                        on_click=editar_tarefa
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.DELETE,
                                        icon_color=ft.colors.RED,
                                        icon_size=20,
                                        on_click= apagar_tarefa
                                    ),
                                ]
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    )
                )
            )
        
        total.value = f'{len(tarefas_criadas.controls)} Criadas'
        task_textfield.value = ''
        page.update()
    
    def editar_tarefa(e: ft.ControlEvent):

        def salvar_edicao():
            if task_textfield.value != '':
                e.control.parent.parent.controls[0].value = task_textfield.value
            
            task_textfield.value = ''
            task_textfield.on_submit = lambda e: criar_tarefa(e)
            salvar_btn.on_click = lambda e: criar_tarefa(e)
            page.update()

        task_textfield.value = e.control.parent.parent.controls[0].value

        task_textfield.on_submit = lambda e: salvar_edicao()
        salvar_btn.on_click = lambda e: salvar_edicao()

        total.value = f'{len(tarefas_criadas.controls)} Criadas'
        page.update()

    def apagar_tarefa(e: ft.ControlEvent):
        tarefas_criadas.controls.remove(e.control.parent.parent.parent)
        total.value = f'{len(tarefas_criadas.controls)} Criadas'
        page.update()

    view = ft.View(
        route='/',
        controls=[
            ft.SafeArea(
                content=ft.Stack(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Text(
                                            value='Task App'.upper(),
                                            color=textcolor,
                                            size=20,
                                            weight='bold'
                                        )
                                    ]
                                ),
                                ft.Divider(
                                    height=1,
                                    color=textcolor,
                                    thickness=2
                                ),
                                ft.ResponsiveRow(
                                    controls=[
                                        task_textfield := ft.TextField(
                                            hint_text='O que vai fazer?',
                                            hint_style=ft.TextStyle(
                                                color=ft.colors.with_opacity(0.4, textcolor),
                                                size=15,
                                                weight='bold'
                                            ),
                                            text_style=ft.TextStyle(
                                                color=textcolor,
                                                size=15,
                                                weight='bold'
                                            ),
                                            border_color=ft.colors.with_opacity(0.4, textcolor),
                                            border_radius=5,
                                            # autofocus=True,
                                            col={'xs':9.8, 'sm': 9.8},
                                            on_submit= lambda e: criar_tarefa(e)
                                        ),
                                        salvar_btn := ft.FloatingActionButton(
                                            icon=ft.icons.ADD,
                                            foreground_color=textcolor,
                                            bgcolor=ft.colors.BLUE,
                                            height=62,
                                            col={'xs':2.2, 'sm': 2.2},
                                            on_click=lambda e: criar_tarefa(e)
                                        )
                                    ]
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text(
                                            value='Descrição',
                                            size=15,
                                            color=textcolor,
                                            weight='bold'
                                        ),
                                        total := ft.Text(
                                            value=f'{0} Criadas',
                                            size=15,
                                            color=textcolor,
                                            weight='bold'
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                ),
                                tarefas_criadas := ft.Column(
                                    controls=[
                                        
                                    ],
                                    height=height * 0.75,
                                    scroll=ft.ScrollMode.ADAPTIVE
                                )
                            ]
                        )
                    ]
                )
            )
        ]
    )

    return view