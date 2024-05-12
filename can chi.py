def tinh_can_chi(nam_duong_lich):
    can = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
    chi = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
    
    t_can = (nam_duong_lich + 6) % 10
    t_chi = (nam_duong_lich + 8) % 12
    
    can_chi = f"{can[t_can]} {chi[t_chi]}"
    print(can_chi)

# Năm dương lịch đển tính can chi
tinh_can_chi(2001)
