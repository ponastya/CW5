from flask import Blueprint, render_template, request, redirect, url_for
from equipment import Equipment
from unit import PlayerUnit, EnemyUnit
from classes import unit_classes
from base import Arena

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates', url_prefix='/')

heroes = {
    "player": NotImplemented,
    "enemy": NotImplemented,
}

arena = Arena()


@main_blueprint.route("/")
def menu_page():
    return render_template("index.html")


@main_blueprint.route("/fight/")
def start_fight():
    arena.start_game(player=heroes['player'], enemy=heroes['enemy'])
    return render_template('fight.html', heroes=heroes)


@main_blueprint.route("/fight/hit")
def hit():
    if arena.game_is_running:
        result = arena.player_hit()
    else:
        result = arena.battle_result

    return render_template('fight.html', heroes=heroes, result=result)


@main_blueprint.route("/fight/use-skill")
def use_skill():
    if arena.game_is_running:
        result = arena.player_use_skill()
    else:
        result = arena.battle_result

    return render_template('fight.html', heroes=heroes, result=result)


@main_blueprint.route("/fight/pass-turn")
def pass_turn():
    if arena.game_is_running:
        result = arena.next_turn()
    else:
        result = arena.battle_result

    return render_template('fight.html', heroes=heroes, result=result)


@main_blueprint.route("/fight/end-fight")
def end_fight():
    return render_template("index.html", heroes=heroes)


@main_blueprint.route("/choose-hero/", methods=['post', 'get'])
def choose_hero():
    if request.method == 'GET':
        header = "Выберите героя"
        equipment = Equipment()
        weapons = equipment.get_weapons_names()
        armors = equipment.get_armors_names()
        result = {
            'header': header,
            'weapons': weapons,
            'armors': armors,
            'classes': unit_classes,
        }
        return render_template('hero_choosing.html', result=result)

    if request.method == 'POST':
        name = request.form['name']
        weapon_name = request.form['weapon']
        armor_name = request.form['armor']
        unit_class_name = request.form['unit_class']

        unit = unit_classes.get(unit_class_name)
        if unit is None:
            return render_template('index.html')
        player = PlayerUnit(name=name, unit_class=unit_classes.get(unit_class_name))

        armor = (Equipment().get_armor(armor_name))
        weapon = (Equipment().get_weapon(weapon_name))
        if armor is None or weapon is None:
            return render_template('index.html')

        player.equip_armor(Equipment().get_armor(armor_name))
        player.equip_weapon(Equipment().get_weapon(weapon_name))
        heroes['player'] = player
        return redirect(url_for('main_blueprint.choose_enemy'))


@main_blueprint.route("/choose-enemy/", methods=['post', 'get'])
def choose_enemy():
    if request.method == 'GET':
        header = "Выберите противника"
        equipment = Equipment()
        weapons = equipment.get_weapons_names()
        armors = equipment.get_armors_names()
        result = {
            'header': header,
            'weapons': weapons,
            'armors': armors,
            'classes': unit_classes,
        }
        return render_template('hero_choosing.html', result=result)

    if request.method == 'POST':
        name = request.form['name']
        weapon_name = request.form['weapon']
        armor_name = request.form['armor']
        unit_class_name = request.form['unit_class']

        unit = unit_classes.get(unit_class_name)
        if unit is None:
            return redirect(url_for('main_blueprint.choose_enemy'))

        enemy = EnemyUnit(name=name, unit_class=unit_classes.get(unit_class_name))

        armor = (Equipment().get_armor(armor_name))
        weapon = (Equipment().get_weapon(weapon_name))
        if armor is None or weapon is None:
            return redirect(url_for('main_blueprint.choose_enemy'))

        enemy.equip_armor(Equipment().get_armor(armor_name))
        enemy.equip_weapon(Equipment().get_weapon(weapon_name))
        heroes['enemy'] = enemy
        return redirect(url_for('main_blueprint.start_fight'))
