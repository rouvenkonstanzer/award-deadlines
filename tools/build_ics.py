import datetime as dt, re, sys

# (award, label, start, end_inclusive or None, kind, confirmed, url, note)
# kind: "frist" gets reminders, "event" none
E = []
def add(award, label, start, end=None, kind="frist", ok=True, url="", note=""):
    E.append(dict(award=award, label=label, start=start, end=end, kind=kind, ok=ok, url=url, note=note))

CL = "https://www.canneslions.com/awards/awards-support/dates-and-fees"
add("Cannes Lions", "Einreichstart", "2027-01-14", kind="event", url=CL, note="Einreichung für Cannes Lions 2027 öffnet.")
add("Cannes Lions", "Preisstufe 1 endet", "2027-03-04", url=CL, note="Danach gelten höhere Gebühren.")
add("Cannes Lions", "Preisstufe 2 endet", "2027-03-18", url=CL, note="Danach steigen die Gebühren erneut.")
add("Cannes Lions", "Preisstufe 3 endet", "2027-04-01", url=CL, note="Letzte Stufe vor der finalen Deadline.")
add("Cannes Lions", "Finale Deadline", "2027-04-08", url=CL, note="23:59 Uhr Ortszeit Cannes. Zulassungszeitraum meist 1. Februar 2026 bis 8. April 2027.")
add("Cannes Lions", "Festival", "2027-06-21", "2027-06-25", kind="event", url=CL, note="Festival und Verleihungen in Cannes.")

DA = "https://www.dandad.org/awards/d-ad-awards"
add("D&AD", "Frist 30 % Rabatt", "2026-12-16", url=DA, note="Zahlung bis 9. Dezember, Einreichung abschließen bis 16. Dezember 2026. Physische Einsendungen bis 13. Januar 2027.")
add("D&AD", "Frist 20 % Rabatt", "2027-02-17", url=DA, note="Zahlung bis 10. Februar, Einreichung abschließen bis 17. Februar 2027.")
add("D&AD", "Frist 10 % Rabatt", "2027-03-17", url=DA, note="Zahlung bis 10. März, Einreichung abschließen bis 17. März 2027.")
add("D&AD", "Finale Deadline", "2027-04-14", url=DA, note="Zahlung bis 7. April, Einreichung abschließen bis 14. April 2027. Physische Einsendungen bis 21. April.")
add("D&AD", "Shortlist", "2027-05-26", kind="event", url=DA)
add("D&AD", "Verleihung", "2027-06-28", kind="event", url=DA, note="Award Ceremony und Bekanntgabe der Pencils.")

OS = "https://oneshow.org/dates/"
add("The One Show", "Advance Deadline", "2026-12-11", url=OS, note="Günstigste Stufe. Die Gebühren steigen mit jeder Frist.")
add("The One Show", "Early Deadline", "2027-01-22", url=OS)
add("The One Show", "Standard Deadline", "2027-02-12", url=OS)
add("The One Show", "Final Deadline", "2027-03-05", url=OS, note="Danach nur noch mit Late Fee.")
add("The One Show", "Creative Week New York", "2027-05-10", "2027-05-14", kind="event", ok=False, url="https://creativeweek.com", note="Geschätzt: 2025 und 2026 lag die Creative Week Mitte Mai, die Show am Freitag. Termin 2027 noch nicht bestätigt.")

ADC = "https://www.adc.de/wettbewerb/adc-wettbewerb-2027/"
add("ADC Deutschland", "Early Bird (10 % Rabatt)", "2026-11-26", url=ADC, note="Für Arbeiten aus 2026. Die Seite des ADC ist noch teils mit 2026 beschriftet, bitte vor dem Einreichen prüfen.")
add("ADC Deutschland", "Teilnahmeschluss Arbeiten 2026", "2027-02-18", url=ADC, note="Reguläre Einreichung für Arbeiten aus 2026. Mit 20 % Late Fee bis 4. März 2027.")
add("ADC Deutschland", "Late Fee Arbeiten 2026 / Schluss Arbeiten 2027", "2027-03-04", url=ADC, note="Letzte Chance für Arbeiten aus 2026 (mit Late Fee). Regulärer Schluss für Arbeiten, die vom 1. Januar bis 15. Februar 2027 veröffentlicht wurden.")
add("ADC Deutschland", "Late Fee Arbeiten 2027", "2027-03-18", url=ADC, note="Mit Late Fee, für Arbeiten aus 2027.")
add("ADC Deutschland", "ADC Festival Hamburg", "2027-06-09", "2027-06-10", kind="event", ok=False, url="https://www.adc.de", note="Geschätzt: 2025 und 2026 lag das Festival Mitte Juni in Hamburg. Termin 2027 noch nicht bestätigt.")

ADCE = "https://adceurope.awardhub.org/dates/"
add("ADC Europe", "Gala Barcelona", "2026-11-20", kind="event", url=ADCE, note="ADCE Awards Gala zum Abschluss der ADCE Creative Week.")
add("ADC Europe", "Deadline 2027", "2027-09-24", ok=False, url=ADCE, note="Geschätzt nach dem Vorjahr (Deadline 25. September 2026). Termin 2027 noch nicht veröffentlicht.")

EB = "https://www.eurobest.com/support/eurobest-awards-entry-guide"
add("Eurobest", "Finale Deadline 2027", "2027-10-14", ok=False, url=EB, note="Geschätzt nach dem Vorjahr (15. Oktober 2026, Einreichstart August, Late Fees ab Mitte September). Termin 2027 noch nicht veröffentlicht.")

EP = "https://www.epica-awards.com/enter"
add("Epica", "Shortlist 2026", "2026-11-25", kind="event", url="https://registration.epica-awards.com/")
add("Epica", "Verleihung 2026", "2026-12-15", kind="event", url="https://registration.epica-awards.com/", note="Endergebnisse am 16. Dezember.")
add("Epica", "Early-Bird-Ende 2027", "2027-09-01", ok=False, url=EP, note="Geschätzt nach dem Vorjahr (Early Bird bis 1. September 2026).")
add("Epica", "Finale Deadline 2027", "2027-10-29", ok=False, url=EP, note="Geschätzt nach dem Vorjahr (Late Entry bis 30./31. Oktober 2026).")

CLIO = "https://clios.com/the-clio-awards/entry-information/key-dates/"
add("Clio Awards", "2. Deadline", "2026-12-11", url=CLIO, note="23:59 Uhr EST, in Deutschland also am 12. Dezember morgens. Die Gebühren steigen nach jeder Frist.")
add("Clio Awards", "3. Deadline", "2027-01-15", url=CLIO, note="23:59 Uhr EST.")
add("Clio Awards", "Finale Deadline", "2027-02-19", url=CLIO, note="23:59 Uhr EST. Physische Einsendungen müssen bis dahin im Clio-Büro sein. Show im Mai 2027 in New York.")

RD = "https://www.red-dot.org/bcd/participate"
add("Red Dot Brands & Communication", "Early-Bird-Ende 2027", "2027-02-12", ok=False, url=RD, note="Geschätzt nach dem Vorjahr (Early Bird 26. Januar bis 13. Februar 2026).")
add("Red Dot Brands & Communication", "Ende reguläre Phase 2027", "2027-04-23", ok=False, url=RD, note="Geschätzt nach dem Vorjahr (regulär bis 24. April 2026).")
add("Red Dot Brands & Communication", "Ende Latecomer 2027", "2027-05-07", ok=False, url=RD, note="Geschätzt nach dem Vorjahr (Latecomer bis 8. Mai 2026).")

IF = "https://www.dezeen.com/competitions/if-design-award-2027/"
add("iF Design Award", "Gewinner 2027", "2027-02-24", kind="event", url=IF, note="Finale Jury vom 16. bis 18. Februar 2027.")
add("iF Design Award", "Early-Bird-Ende 2028", "2027-06-25", ok=False, url="https://ifdesign.com", note="Geschätzt nach dem Vorjahr (26. Juni 2026). Gebühren 2027 waren 300 / 400 / 500 Euro pro Einreichung.")
add("iF Design Award", "Reguläre Deadline 2028", "2027-09-17", ok=False, url="https://ifdesign.com", note="Geschätzt nach dem Vorjahr (18. September 2026).")
add("iF Design Award", "Finale Deadline 2028", "2027-11-03", ok=False, url="https://ifdesign.com", note="Geschätzt nach dem Vorjahr (2. bzw. 4. November 2026).")

GDA = "https://www.german-design-award.com/en/news/detail/german-design-awards-2027-call-for-entries"
add("German Design Award", "Award Show 2027", "2027-01-29", kind="event", url=GDA, note="Verleihung in Frankfurt am Main.")
add("German Design Award", "Einreichschluss 2028", "2027-09-10", ok=False, url="https://www.german-design-award.com/en", note="Geschätzt nach dem Vorjahr (11. September 2026). Gebühren steigen gestaffelt, im Vorjahr ab Mitte Juni.")

AM = "https://www.annual-multimedia.de"
add("Annual Multimedia", "Einreichschluss 2028", "2027-08-27", ok=False, url=AM, note="Geschätzt: in den Vorjahren lag der Schluss Ende August (2025: 28. August). Termin noch nicht veröffentlicht.")

TDC = "https://enter.tdc.org/"
add("Type Directors Club (TDC73)", "Early Deadline", "2027-01-22", url=TDC, note="Günstigste Stufe. Gebühren je nach Region.")
add("Type Directors Club (TDC73)", "Standard Deadline", "2027-02-12", url=TDC)
add("Type Directors Club (TDC73)", "Final Deadline", "2027-03-05", url=TDC, note="Gewinner werden im Mai 2027 bekanntgegeben.")

def esc(s): return s.replace("\\", "\\\\").replace(";", "\;").replace(",", "\\,").replace("\n", "\\n")
def fold(line):
    b = line.encode("utf-8"); out = []; cur = b""
    i = 0; first = True
    chars = list(line); buf = ""
    for ch in chars:
        limit = 75 if first else 74
        if len((buf + ch).encode("utf-8")) > limit:
            out.append(buf if first else " " + buf); buf = ch; first = False
        else: buf += ch
    out.append(buf if first else " " + buf)
    return "\r\n".join(out)
def slug(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

stamp = dt.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
L = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Rouven Konstanzer//Award-Deadlines//DE", "CALSCALE:GREGORIAN", "METHOD:PUBLISH",
     "X-WR-CALNAME:Award-Deadlines", "X-WR-CALDESC:Fristen\\, Shortlists und Verleihungen der wichtigsten Kreativ-Awards. Mit ≈ markierte Termine sind geschätzt.",
     "X-WR-TIMEZONE:Europe/Berlin", "REFRESH-INTERVAL;VALUE=DURATION:PT12H", "X-PUBLISHED-TTL:PT12H"]
for e in E:
    s = dt.date.fromisoformat(e["start"]); en = dt.date.fromisoformat(e["end"] or e["start"]) + dt.timedelta(days=1)
    title = ("" if e["ok"] else "≈ ") + f'{e["award"]} · {e["label"]}' + ("" if e["ok"] else " (geschätzt)")
    desc = ("Status: bestätigt laut offizieller Quelle." if e["ok"] else "Status: GESCHÄTZT, noch nicht offiziell. Bitte vor dem Einreichen prüfen.") + ("\n\n" + e["note"] if e["note"] else "") + ("\n\nQuelle: " + e["url"] if e["url"] else "")
    L += ["BEGIN:VEVENT", f'UID:{slug(e["award"])}-{slug(e["label"])}-{e["start"]}@award-deadlines.rouvenkonstanzer', f"DTSTAMP:{stamp}",
          f"DTSTART;VALUE=DATE:{s:%Y%m%d}", f"DTEND;VALUE=DATE:{en:%Y%m%d}", "SUMMARY:" + esc(title), "DESCRIPTION:" + esc(desc),
          "TRANSP:TRANSPARENT", "CATEGORIES:" + ("Frist" if e["kind"] == "frist" else "Termin")]
    if e["url"]: L.append("URL:" + e["url"])
    if e["kind"] == "frist":
        for trig, txt in (("-P14D", "in 14 Tagen"), ("-P2D", "in 2 Tagen")):
            L += ["BEGIN:VALARM", "ACTION:DISPLAY", f"TRIGGER:{trig}", "DESCRIPTION:" + esc(f'{e["award"]}: {e["label"]} {txt}'), "END:VALARM"]
    L.append("END:VEVENT")
L.append("END:VCALENDAR")
open(sys.argv[1], "w", encoding="utf-8", newline="").write("\r\n".join(fold(l) for l in L) + "\r\n")
print(len(E), "events,", sum(1 for e in E if not e["ok"]), "estimated")
