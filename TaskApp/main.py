import flet as ft
from views.home import home

def main(page: ft.Page):
    page.title = page.route

    WIDTH: int = page.width
    HEIGHT: int = page.height

    def router(route):
        page.views.clear()

        if page.route == '/':
            page.views.append(home(page, WIDTH, HEIGHT))
        
        page.title = page.route
        page.update()
    
    page.on_route_change = router
    page.go(page.route)

if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)