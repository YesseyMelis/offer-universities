import pandas
import xlrd
from universities.models import City, University, Subject, Speciality, Profession

dataEN = pandas.read_excel('data/Data.xlsx', sheet_name="dataEN")
dataRU = pandas.read_excel('data/Data.xlsx', sheet_name="dataRU")
dataKZ = pandas.read_excel('data/Data.xlsx', sheet_name="dataKZ")
profEN = pandas.read_excel('data/Data.xlsx', sheet_name="profEN")
profRU = pandas.read_excel('data/Data.xlsx', sheet_name="profRU")
profKZ = pandas.read_excel('data/Data.xlsx', sheet_name="profKZ")

def parse_city():
    en_cities = dataEN.get('city')
    ru_cities = dataRU.get('city')
    kz_cities = dataKZ.get('city')
    for en, ru, kz in zip(en_cities, ru_cities, kz_cities):
        en = en.strip()
        ru = ru.strip()
        kz = kz.strip()
        if not City.objects.filter(name_en=en, name_ru=ru, name_kz=kz).exists():
            City.objects.create(name_en=en, name_ru=ru, name_kz=kz)

def parse_university():
    codes = dataEN.get('code')
    en_univer = dataEN.get('university')
    ru_univer = dataRU.get('university')
    kz_univer = dataKZ.get('university')
    cities = dataEN.get('city')
    sites = dataEN.get('site')
    for code, en, ru, kz, city, site in zip(codes, en_univer, ru_univer, kz_univer, cities, sites):
        en = en.split('"')[1].strip() if '"' in en else en.strip()
        ru = ru.split('"')[1].strip() if '"' in ru else ru.strip()
        kz = kz.split('"')[1].strip() if '"' in kz else kz.strip()
        city = city.strip()
        c = City.objects.filter(name_en__icontains=city)
        univer = University.objects.filter(code=code, name_en__icontains=en, name_ru__icontains=ru, name_kz__icontains=kz, city__in=c, site=site)
        if not univer.exists():
            University.objects.create(code=code, name_en=en, name_ru=ru, name_kz=kz, city=c.first(), site=site)

def parse_subjects():
    en_subject_1 = dataEN.get('subject1')
    ru_subject_1 = dataRU.get('subject1')
    kz_subject_1 = dataKZ.get('subject1')
    en_subject_2 = dataEN.get('subject2')
    ru_subject_2 = dataRU.get('subject2')
    kz_subject_2 = dataKZ.get('subject2')
    for en1, ru1, kz1, en2, ru2, kz2 in zip(en_subject_1, ru_subject_1, kz_subject_1, en_subject_2, ru_subject_2, kz_subject_2):
        en1 = en1.strip()
        ru1 = ru1.strip()
        kz1 = kz1.strip()
        en2 = en2.strip()
        ru2 = ru2.strip()
        kz2 = kz2.strip()
        sub1 = Subject.objects.filter(name_en__icontains=en1, name_ru__icontains=ru1, name_kz__icontains=kz1)
        sub2 = Subject.objects.filter(name_en__icontains=en2, name_ru__icontains=ru2, name_kz__icontains=kz2)
        if not sub1.exists():
            Subject.objects.create(name_en=en1, name_ru=ru1, name_kz=kz1)
        if not sub2.exists():
            Subject.objects.create(name_en=en2, name_ru=ru2, name_kz=kz2)


def parse_speciality():
    ciphers = dataEN.get('cipher')
    en_special = dataEN.get('speciality')
    ru_special = dataRU.get('speciality')
    kz_special = dataKZ.get('speciality')
    en_desc = dataEN.get('description')
    ru_desc = dataRU.get('description')
    kz_desc = dataKZ.get('description')
    univer = dataEN.get('university')
    sub1 = dataEN.get('subject1')
    sub2 = dataEN.get('subject2')
    total_grant = dataEN.get('total_grant')
    grant_rus = dataEN.get('grant_rus')
    grant_kaz = dataEN.get('grant_kaz')
    for cph, ens, rus, kzs, end, rud, kzd, uni, s1, s2, total, grus, gkaz in zip(
            ciphers,
            en_special,
            ru_special,
            kz_special,
            en_desc,
            ru_desc,
            kz_desc,
            univer,
            sub1,
            sub2,
            total_grant,
            grant_rus,
            grant_kaz
    ):
        cph = cph.strip()
        ens = ens.strip()
        rus = rus.strip()
        kzs = kzs.strip()
        end = end.strip()
        rud = rud.strip()
        kzd = kzd.strip()
        uni = uni.split('"')[1].strip() if '"' in uni else uni.strip()
        s1 = s1.strip()
        s2 = s2.strip()
        total = int(total)
        grant_ru = int(grus) if type(grus) == int else 0
        grant_kz = int(gkaz) if type(gkaz) == int else 0

        unik = University.objects.filter(name_en__icontains=uni)
        subject1 = Subject.objects.filter(name_en__icontains=s1)
        subject2 = Subject.objects.filter(name_en__icontains=s2)
        speciality = Speciality.objects.filter(
            code=cph,
            name_en=ens,
            name_ru=rus,
            name_kz=kzs,
            description_en=end,
            description_ru=rud,
            description_kz=kzd,
            university__in=unik,
            first_subject__in=subject1,
            second_subject__in=subject2,
            total_grant=total,
            grant_kaz=grant_kz,
            grant_rus=grant_ru
        )
        if not speciality.exists():
            Speciality.objects.create(
                code=cph,
                name_en=ens,
                name_ru=rus,
                name_kz=kzs,
                description_en=end,
                description_ru=rud,
                description_kz=kzd,
                university=unik.first(),
                first_subject=subject1.first(),
                second_subject=subject2.first(),
                total_grant=total,
                grant_kaz=grant_kz,
                grant_rus=grant_ru
            )

def parse_profession():
    en_spec = profEN.get('speciality')
    en_prof = profEN.get('profession')
    ru_prof = profRU.get('profession')
    kz_prof = profKZ.get('profession')
    for sp, en, ru, kz in zip(en_spec, en_prof, ru_prof, kz_prof):
        sp = sp.strip()
        en = en.strip()
        ru = ru.strip()
        kz = kz.strip()
        spec = Speciality.objects.filter(name_en__icontains=sp)
        if spec.exists():
            prof = Profession.objects.filter(name_en__icontains=en, name_ru__icontains=ru, name_kz__icontains=kz, speciality__in=spec)
            if not prof.exists():
                Profession.objects.create(name_en=en, name_ru=ru, name_kz=kz, speciality=spec.first())
