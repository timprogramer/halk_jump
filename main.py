import wrap,time

#переменные
shirena=900
vysota=600
y=vysota-79


wrap.world.create_world(shirena,vysota,200,200)
wrap.world.set_back_color(255,0,0)

#создание платформ
wrap.sprite.add("mario-items",45,y,"cloud_platform")
wrap.sprite.add("mario-items",shirena-45,y,"cloud_platform")
#wrap.sprite.add("mario-items",x4,y1,"cloud_platform")

#создание персонажа
wrap.add_sprite_dir("мои спрайты")
wrap.sprite.add("стичь",45,y-50,"stich")

#прыжок
polovinapyti=shirena/2
wrap.actions.move_to(2,polovinapyti,150)
wrap.actions.move_to(2,polovinapyti*2-45,y-50)
