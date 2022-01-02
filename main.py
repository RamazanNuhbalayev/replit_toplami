from math import *

#deyisenler


print("Eger üçbucaq beraberyanlıdırsa terefleri ve \n oturacağı melumdursa 1-i seçin")
print("\n")


def medi_ot_emel_get_buc_der_ile_1_ci_usul(u_oturacagi,yan_terefin_yarisi,ot_bit_buc_der_ile):
  sin_ot_bit_buc_rad_ile=sin(radians(ot_bit_buc_der_ile))
  ələ d.kotangens_ot_bit_buc_rad_ile=1/tan(radians(ot_bit_buc_der_ile))
  ctg_medi_ot_emel_get_buc_rad_ile_1=(u_oturacagi-(yan_terefin_yarisi*sin_ot_bit_buc_rad_ile*kotangens_ot_bit_buc_rad_ile))/yan_terefin_yarisi*sin_ot_bit_buc_rad_ile
  medi_ot_emel_get_buc_rad_ile_1_ci_usul=1/atan(ctg_medi_ot_emel_get_buc_rad_ile_1)
  medi_ot_emel_get_buc_derece_ile_1_ci_usul=degrees(medi_ot_emel_get_buc_rad_ile_1_ci_usul)
  print("Medianin oturacaq ile emele getirdiyi")
  print("bucağın derece ölçüsü I usul:",medi_ot_emel_get_buc_derece_ile_1_ci_usul,"\n")
  return medi_ot_emel_get_buc_derece_ile_1_ci_usul


def ucbucaq():
  case=int(input("seçin:"))
  if case==1:
      u_yan_terefi=float(input("Üçbucağın yan terefini santimetrle ifade edin : "))
      print("\n")
      u_oturacagi=float(input("Üçbucağın oturacağını santimetrle ifade edin : "))
      print("\n")
      yan_terefin_kv=pow(u_yan_terefi,2)
      u_oturacagin_yarisi=u_oturacagi/2
      u_oturacagin_yarisinin_kv=pow(u_oturacagin_yarisi,2)
      u_y_t_kv_cix_o_y_kv=yan_terefin_kv-u_oturacagin_yarisinin_kv
      u_hund_tenb_median=pow(u_y_t_kv_cix_o_y_kv,0.5)
      ucb_sahesi=u_hund_tenb_median*u_oturacagin_yarisi
      #oturacaq qarşısındakı bucağın yarısının tangensini tapaq 
      tg_ot_qar_buc_yar=u_oturacagin_yarisi/u_hund_tenb_median #tangens oturacaq qarşısındakı bucağın yarısı
      ot_qar_buc_yar_rad_ile=atan(tg_ot_qar_buc_yar) #oturacaq qarşısındakı bucağın yarısı radian ile
      ot_qar_buc_yar_der_ile=degrees(ot_qar_buc_yar_rad_ile) #oturacaq qarşısındakı bucağın yarısı derece ile
      ot_qar_buc_der_ile=ot_qar_buc_yar_der_ile*2 #oturacaq qarşısındakı bucağın qiymeti derece ile
      ot_bit_buc_der_ile=(180-ot_qar_buc_der_ile)/2
      yan_terefin_yarisi=u_yan_terefi/2

      sahe_median=0.5*yan_terefin_yarisi*u_oturacagi*sin(radians(ot_bit_buc_der_ile))
      medi_ot_emel_get_buc_der_ile_1_ci_usul(u_oturacagi,yan_terefin_yarisi,ot_bit_buc_der_ile)

      


      ctg_medi_ot_emel_get_buc_rad_ile_2_ci_usul=((u_oturacagi**2)-2*sahe_median*(1/tan(radians(ot_bit_buc_der_ile))))/2*sahe_median
      medi_ot_emel_get_buc_der_ile_2_ci_usul=degrees(1/atan(ctg_medi_ot_emel_get_buc_rad_ile_2_ci_usul))
      
      
      medi_yan_emel_buc=180-medi_ot_emel_get_buc_der_ile_1_ci_usul(u_oturacagi,yan_terefin_yarisi,ot_bit_buc_der_ile)-ot_bit_buc_der_ile #medianin yan teref ile emele getirdiyi oturcaq qarşısındakı bucaq
      medi_yan_emel_buc_2_ci_usul=180-medi_ot_emel_get_buc_der_ile_2_ci_usul-ot_bit_buc_der_ile #medianin yan teref ile emele getirdiyi oturcaq qarşısındakı bucaq 2 ci usul
      kotangens_medi_ot_emel_get_buc_der_ile=1/tan(radians(medi_ot_emel_get_buc_der_ile_2_ci_usul))
      kotangens_medi_yan_emel_buc=1/tan(radians(medi_yan_emel_buc))
      med_bit_buc_kotangensler_cemi=kotangens_medi_ot_emel_get_buc_der_ile+kotangens_medi_yan_emel_buc
      median_uz_kv=2*sahe_median*med_bit_buc_kotangensler_cemi
      median_uz=pow(median_uz_kv,0.5)
      
      print("hündürlüyü tenboleni ve mediani hamisi bir birine beraberdir : ",u_hund_tenb_median,"\n")
      print("Üçbucağın sahesi ise : ",ucb_sahesi,"ya beraberdir\n")
      print("Beraberyanlı üçbucağın oturacağı qarşısındakı tepe bucağı:",ot_qar_buc_der_ile,"\n")
      print("Beraberyanlı üçbucağın oturacağa bitişik bucağı:",ot_bit_buc_der_ile,"\n")
      print("medianalti sahe",sahe_median,"\n")
      print("Yan terefe cekilmis medianin oturacaq ile emele getirdiyi bucagin derece olcusu",medi_ot_emel_get_buc_der_ile_1_ci_usul(u_oturacagi,yan_terefin_yarisi,ot_bit_buc_der_ile))
      print("Yan terefe cekilmis medianin oturacaq ile emele getirdiyi bucagin derece olcusu_2_ci_usul",medi_ot_emel_get_buc_der_ile_2_ci_usul,"\n")
      print("Yan terefe cekilmis medianin yan teref ile emele getirdiyi oturcaq qarşısındakı bucaq",medi_yan_emel_buc,"\n")
      print("Yan terefe cekilmis medianin yan teref ile emele getirdiyi oturcaq qarşısındakı bucaq 2ci usul",medi_yan_emel_buc_2_ci_usul,"\n")
      print("Yan terefe cekilmis medianin uzunluğu: ",median_uz,"\n")
      
      ucbucaq()
  return 0
ucbucaq()
