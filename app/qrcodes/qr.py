import qrcode


def make_ticket_qr(ticket_data):
    qr_data = f"ticket_id:{ticket_data['id'], ticket_data['title'], ticket_data['date']}"
    img = qrcode.make(qr_data)
    img_path = f"app/qrcodes/img/{ticket_data['id']}.png"
    img.save(img_path)

    return img_path