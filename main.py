import functions
import msg

produtos = {}
cat = {}
terminar = len(msg.ACCOES)

while True:
    functions.draw_menu()
    match functions.check_input(input(msg.ACCAO)):
        case 1:
            p, c = functions.set_product(catalogo=cat)
            print(f' O meu catálogo tem {len(c)} produtos.')
        case 2:
            functions.get_product()
        case 3:
            functions.update_product()
        case 4:
            functions.delete_product()
        case terminar:
            print(msg.MSG_FINAL)
            break










