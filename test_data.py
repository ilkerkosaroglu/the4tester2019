# All test cases created by Burak Akkaya
FS001 = ["/", "d",
         ["studio", "d", ["zero.py", "f"], ["thakur.jpg", "f"]],
         ["home", "d",
          ["psychology", "d", ["trauma", "d", ["pills.py","f"], ["coffee.jpg","f"]], ["versus.py", "f"],
           ["crazy", "d", ["stars.jpg", "f"], ["custody.avi", "f"]]],
          ["street", "d", ["ritman.py", "f"], ["future.txt", "f"]]]]
C001 = ["cd home/psychology/",
        "mkdir ../psychology/crazy/prison",
        "rmdir /home/./street",
        "cd .././..//studio",
        "rm ../home/psychology/versus.py",
        "cp zero.py /home/"]
R001 = ("SUCCESS", ["/", "d",
                    ["studio", "d", ["zero.py", "f"], ["thakur.jpg", "f"]],
                    ["home", "d",
                     ["psychology", "d", ["trauma", "d", ["pills.py"], ["coffee.jpg"]],
                      ["crazy", "d", ["stars.jpg", "f"],
                       ["custody.avi", "f"], ["prison", "d"]]], ["zero.py", "f"]]], "/studio")

FS002 = ["/", "d",
         ["movies", "d", ["2018", "d"], ["2010", "d"]],
         ["series", "d", ["netflix", "d", ["black.avi", "f"], ["mirror.mkv", "f"]]],
         ["photos", "d"],
         ["musics", "d", ["ajdar", "d", ["turp_gibi.mp3", "f"]], ["tarkan", "d"], ["2010", "d"]]]
C002 = ["cd series/netflix",
        "rmdir .././/../musics/ajdar",
        "cd .."]
R002 = ("ERROR", "rmdir .././/../musics/ajdar", "/series/netflix")

FS003 = ["/", "d",
         ["movies", "d", ["2018", "d"], ["2010", "d"]],
         ["series", "d", ["netflix", "d", ["black.avi", "f"], ["mirror.mkv", "f"]]],
         ["photos", "d"],
         ["musics", "d", ["ajdar", "d", ["turp_gibi.mp3", "f"]], ["tarkan", "d"], ["2010", "d"]]]
C003 = ["cd series/netflix",
        "exec black.avi",
        "exec /musics/ajdar/turp_gibi.mp3",
        "rm ../..//movies/2018",
        "cd /movies/2018"]
R003 = ("ERROR", "rm ../..//movies/2018", "/series/netflix")

FS004 = ["/", "d",
         ["movies", "d", ["2018", "d"], ["2010", "d"]],
         ["series", "d", ["netflix", "d", ["black.avi", "f"], ["mirror.mkv", "f"]]],
         ["photos", "d"],
         ["musics", "d", ["ajdar", "d", ["turp_gibi.mp3", "f"]], ["tarkan", "d"], ["2010", "d"]]]
C004 = ["cd photos",
        "rm ../series/netflix/black.avi",
        "cp /movies/2010 ../musics/",
        "exec /series/netflix/mirror.mkv"]
R004 = ("ERROR", "cp /movies/2010 ../musics/", "/photos")

FS005 = ["/", "d",
         ["movies", "d", ["2018", "d"], ["2010", "d"]],
         ["series", "d", ["netflix", "d", ["black.avi", "f"], ["mirror.mkv", "f"]]],
         ["photos", "d"],
         ["musics", "d", ["ajdar", "d", ["turp_gibi.mp3", "f"]], ["tarkan", "d"], ["2010", "d"]]]
C005 = ["cd musics/tarkan",
        "rmdir ../.././//./musics/tarkan"]
R005 = ("SUCCESS", ["/", "d",
                    ["movies", "d", ["2018", "d"], ["2010", "d"]],
                    ["series", "d", ["netflix", "d", ["black.avi", "f"], ["mirror.mkv", "f"]]],
                    ["photos", "d"],
                    ["musics", "d", ["ajdar", "d", ["turp_gibi.mp3", "f"]], ["2010", "d"]]], "/musics/tarkan")

FS006 = ["/", "d",
         ["movies", "d", ["2018", "d"], ["2010", "d"]],
         ["series", "d", ["netflix", "d", ["black.avi", "f"], ["mirror.mkv", "f"]]],
         ["photos", "d"],
         ["musics", "d", ["ajdar", "d", ["turp_gibi.mp3", "f"]], ["tarkan", "d"], ["2010", "d"]]]
C006 = ["exec movies/2018"]
R006 = ("ERROR", "exec movies/2018", "/")

FS007 = ["/", "d",
         ["downloads", "d"], ["documents", "d", ["photoshop", "d"]],
         ["work", "d", ["cv.pdf", "f"], ["photos", "d"]],
         ["plans", "d", ["website", "d", ["index.php", "f"]]],
         ["games", "d"], ["software", "d", ["valecnik_rpg", "d", ["main.py", "f"]]], ["other", "d"]]
C007 = ["cd software",
        "mkdir ../games/finished",
        "cp valecnik_rpg /games/finished/",
        "cd ..//games/finished/valecnik_rpg"]
R007 = ("SUCCESS", ["/", "d",
                    ["downloads", "d"], ["documents", "d", ["photoshop", "d"]],
                    ["work", "d", ["cv.pdf", "f"], ["photos", "d"]],
                    ["plans", "d", ["website", "d", ["index.php", "f"]]],
                    ["games", "d", ["finished", "d", ["valecnik_rpg", "d", ["main.py", "f"]]]],
                    ["software", "d", ["valecnik_rpg", "d", ["main.py", "f"]]], ["other", "d"]],
        "/games/finished/valecnik_rpg")

FS008 = ["/", "d",
         ["downloads", "d"], ["documents", "d", ["photoshop", "d"]],
         ["work", "d", ["cv.pdf", "f"], ["photos", "d"]],
         ["plans", "d", ["website", "d", ["index.php", "f"]]],
         ["games", "d"], ["software", "d", ["valecnik_rpg", "d", ["main.py", "f"]]], ["other", "d"]]
C008 = ["cd work",
        "cd .../plans",
        "cd ../*"]
R008 = ("ERROR", "cd .../plans", "/work")

FS009 = ["/", "d",
         ["downloads", "d"], ["documents", "d", ["photoshop", "d"]],
         ["work", "d", ["cv.pdf", "f"], ["photos", "d"]],
         ["plans", "d", ["website", "d", ["index.php", "f"]]],
         ["games", "d"], ["software", "d", ["valecnik_rpg", "d", ["main.py", "f"]]], ["other", "d"]]
C009 = ["cd plans/website/index.php"]
R009 = ("ERROR", "cd plans/website/index.php", "/")

FS010 = ["/", "d",
         ["downloads", "d"], ["documents", "d", ["photoshop", "d"]],
         ["work", "d", ["cv.pdf", "f"], ["photos", "d"]],
         ["plans", "d", ["website", "d", ["index.php", "f"]]],
         ["games", "d"], ["software", "d", ["valecnik_rpg", "d", ["main.py", "f"]]], ["other", "d"]]
C010 = ["cd software/valecnik_rpg",
        "rmdir ../../work",
        "cd /work"]
R010 = ("ERROR", "cd /work", "/software/valecnik_rpg")

FS011 = ["/", "d",
         ["downloads", "d"], ["documents", "d", ["photoshop", "d"]],
         ["work", "d", ["cv.pdf", "f"], ["photos", "d"]],
         ["plans", "d", ["website", "d", ["index.php", "f"]]],
         ["games", "d"], ["software", "d", ["valecnik_rpg", "d", ["main.py", "f"]]], ["other", "d"]]
C011 = ["cd plans/*"]
R011 = ("ERROR", "cd plans/*", "/")

FS012 = ["/", "d",
         ["fire", "d"], ["water", "d", ["sea", "d"], ["lake", "d"]],
         ["earth", "d", ["mountain.jpg", "f"]], ["air", "d"]]
C012 = ["cd earth",
        "rm .././water/sea"]
R012 = ("ERROR", "rm .././water/sea", "/earth")

FS013 = ["/", "d",
         ["fire", "d"], ["water", "d", ["sea", "d"], ["lake", "d"]],
         ["earth", "d", ["mountain.jpg", "f"]], ["air", "d"]]
C013 = ["cd water/sea",
        "rmdir /earth/mountain.jpg"]
R013 = ("ERROR", "rmdir /earth/mountain.jpg", "/water/sea")

FS014 = ["/", "d",
         ["fire", "d"], ["water", "d", ["sea", "d"], ["lake", "d"]],
         ["earth", "d", ["mountain.jpg", "f"]], ["air", "d"]]
C014 = ["cd fire",
        "rmdir .."]
R014 = ("ERROR", "rmdir ..", "/fire")

FS015 = ["/", "d",
         ["fire", "d"], ["water", "d", ["sea", "d"], ["lake", "d"]],
         ["earth", "d", ["mountain.jpg", "f"]], ["air", "d"]]
C015 = ["cp earth/mountain.jpg /water/sea/",
        "cd earth",
        "rm mountain.jpg",
        "exec ../water/sea/mountain.jpg"]
R015 = ("SUCCESS",
        ["/", "d", ["fire", "d"], ["water", "d", ["sea", "d"], ["lake", "d"]], ["earth", "d", ["mountain.jpg", "f"]],
         ["air", "d"]], "/earth")

FS016 = ["/", "d",
         ["the1", "d"],
         ["the2", "d", ["the", "d", ["first.txt", "f"], ["the2.py", "f"]]],
         ["the3", "d", ["the", "d", ["the3.py", "f"]], ["rules.pdf", "f"]],
         ["the4", "d"]]
C016 = ["cp the3/the the4",
        "cd the4/the",
        "exec the3.py"]
R016 = ("SUCCESS", ["/", "d",
                    ["the1", "d"],
                    ["the2", "d", ["the", "d", ["first.txt", "f"], ["the2.py", "f"]]],
                    ["the3", "d", ["the", "d", ["the3.py", "f"]], ["rules.pdf", "f"]],
                    ["the4", "d", ["the", "d", ["the3.py", "f"]]]], "/the4/the")

FS017 = ["/", "d",
         ["the1", "d"],
         ["the2", "d", ["the", "d", ["first.txt", "f"], ["the2.py", "f"]]],
         ["the3", "d", ["the", "d", ["the3.py", "f"]], ["rules.pdf", "f"]],
         ["the4", "d"]]
C017 = ["rmdir the3/the",
        "cd the2/the"]
R017 = ("SUCCESS", ["/", "d",
                    ["the1", "d"],
                    ["the2", "d", ["the", "d", ["first.txt", "f"], ["the2.py", "f"]]],
                    ["the3", "d", ["rules.pdf", "f"]],
                    ["the4", "d"]], "/the2/the")

FS018 = ["/", "d",
         ["the1", "d"],
         ["the2", "d", ["the", "d", ["first.txt", "f"], ["the2.py", "f"]]],
         ["the3", "d", ["the", "d", ["the3.py", "f"]], ["rules.pdf", "f"]],
         ["the4", "d"]]
C018 = ["mkdir the1/the",
        "cd the1/the",
        "mkdir /the3/the"]
R018 = ("ERROR", "mkdir /the3/the", "/the1/the")

FS019 = ["/", "d",
         ["the1", "d"],
         ["the2", "d", ["the", "d", ["first.txt", "f"], ["the2.py", "f"]]],
         ["the3", "d", ["the", "d", ["the3.py", "f"]], ["rules.pdf", "f"]],
         ["the4", "d"]]
C019 = ["exec the2/the/first.txt",
        "cd the3",
        "exec the/the3.py",
        "rm ../the2/the"]
R019 = ("ERROR", "rm ../the2/the", "/the3")

FS020 = ["/", "d",
         ["the1", "d"],
         ["the2", "d", ["the", "d", ["first.txt", "f"], ["the2.py", "f"]]],
         ["the3", "d", ["the", "d", ["the3.py", "f"]], ["rules.pdf", "f"]],
         ["the4", "d"]]
C020 = ["cp the3 the2/",
        "rmdir the2/the3/the",
        "cd the2/the/"]
R020 = ("SUCCESS", ["/", "d",
                    ["the1", "d"],
                    ["the2", "d", ["the", "d", ["first.txt", "f"], ["the2.py", "f"]],
                     ["the3", "d", ["rules.pdf", "f"]]],
                    ["the3", "d", ["the", "d", ["the3.py", "f"]], ["rules.pdf", "f"]],
                    ["the4", "d"]], "/")

FS021 = ["/", "d",
         ["first_line", "d", ["first_column", "d", ["a.txt", "f"], ["b.txt", "f"]],
          ["second_column", "d", ["a.txt", "f"], ["b.txt", "f"]]],
         ["second_line", "d", ["first_column", "d", ["a.txt", "f"], ["b.txt", "f"]],
          ["second_column", "d", ["a.txt", "f"], ["b.txt", "f"]]]]
C021 = ["cd second_line/first_column",
        "exec a.txt",
        "rmdir ../../first_line/second_column"]
R021 = ("ERROR", "rmdir ../../first_line/second_column", "/second_line/first_column")

FS022 = ["/", "d",
         ["first_line", "d", ["first_column", "d", ["a.txt", "f"], ["b.txt", "f"]],
          ["second_column", "d", ["a.txt", "f"], ["b.txt", "f"]]],
         ["second_line", "d", ["first_column", "d", ["a.txt", "f"], ["b.txt", "f"]],
          ["second_column", "d", ["a.txt", "f"], ["b.txt", "f"]]]]
C022 = ["mkdir second_line/first_column/alt_table",
        "cp second_line/first_column first_line/first_column"]
R022 = ("SUCCESS", ["/", "d",
                    ["first_line", "d", ["first_column", "d", ["a.txt", "f"], ["b.txt", "f"],
                                         ["first_column", "d", ["a.txt", "f"], ["b.txt", "f"], ["alt_table", "d"]]],
                     ["second_column", "d", ["a.txt", "f"], ["b.txt", "f"]]],
                    ["second_line", "d", ["first_column", "d", ["a.txt", "f"], ["b.txt", "f"], ["alt_table", "d"]],
                     ["second_column", "d", ["a.txt", "f"], ["b.txt", "f"]]]], "/")

FS023 = ["/", "d",
         ["first_line", "d", ["first_column", "d", ["a.txt", "f"], ["b.txt", "f"]],
          ["second_column", "d", ["a.txt", "f"], ["b.txt", "f"]]],
         ["second_line", "d", ["first_column", "d", ["a.txt", "f"], ["b.txt", "f"]],
          ["second_column", "d", ["a.txt", "f"], ["b.txt", "f"]]]]
C023 = ["cd second_line",
        "rmdir first_column"]
R023 = ("ERROR", "rmdir first_column", "/second_line")

FS024 = ["/", "d",
         ["first_line", "d", ["first_column", "d", ["a.txt", "f"], ["b.txt", "f"]],
          ["second_column", "d", ["a.txt", "f"], ["b.txt", "f"]]],
         ["second_line", "d", ["first_column", "d", ["a.txt", "f"], ["b.txt", "f"]],
          ["second_column", "d", ["a.txt", "f"], ["b.txt", "f"]]]]
C024 = ["cd first_line/second_column",
        "cp a.txt /second_line/",
        "rm a.txt"]
R024 = ("SUCCESS", ["/", "d",
                    ["first_line", "d", ["first_column", "d", ["a.txt", "f"], ["b.txt", "f"]],
                     ["second_column", "d", ["b.txt", "f"]]],
                    ["second_line", "d", ["first_column", "d", ["a.txt", "f"], ["b.txt", "f"]],
                     ["second_column", "d", ["a.txt", "f"], ["b.txt", "f"]], ["a.txt", "f"]]],
        "/first_line/second_column")

FS025 = ["/", "d",
         ["first_line", "d", ["first_column", "d", ["a.txt", "f"], ["b.txt", "f"]],
          ["second_column", "d", ["a.txt", "f"], ["b.txt", "f"]]],
         ["second_line", "d", ["first_column", "d", ["a.txt", "f"], ["b.txt", "f"]],
          ["second_column", "d", ["a.txt", "f"], ["b.txt", "f"]]]]
C025 = ["exec first_line/second_column/a.txt",
        "cd first_line/second_column",
        "rm a.txt",
        "rm b.txt",
        "rmdir ../second_column"]
R025 = ("SUCCESS", ["/", "d",
                    ["first_line", "d", ["first_column", "d", ["a.txt", "f"], ["b.txt", "f"]]],
                    ["second_line", "d", ["first_column", "d", ["a.txt", "f"], ["b.txt", "f"]],
                     ["second_column", "d", ["a.txt", "f"], ["b.txt", "f"]]]], "/first_line/second_column")
