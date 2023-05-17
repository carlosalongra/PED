require "minitest/autorun"
require "./partida.rb"

class TestPartida < Minitest::Test
  
  def test_dummy
    number = 5
    assert_equal 5, number
  end

  def test_numero_rondas_correcto
    partida = creador_de_partidas([[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]])
    assert_equal 10, partida.rondas.length()
  end    
 
  def test_sumar_puntos_mas_basico
    partida = creador_de_partidas([[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]])
    assert_equal 0, partida.sumar_puntos()
  end

  def test_sumar_puntos_menos_basico
    partida = creador_de_partidas([[4,2],[0,0],[0,0],[0,0],[6,0],[9,0],[0,0],[0,0],[0,0],[0,0]])
    assert_equal 21, partida.sumar_puntos()
  end

  def test_rondas_no_suman_mas_de_10
    partida = creador_de_partidas([[4,2],[0,0],[0,0],[0,0],[6,0],[9,0],[0,0],[0,0],[0,0],[0,0]])
    assert_equal true, partida.check_rondas()
  end

  def test_rondas_suman_mas_de_10
    partida = creador_de_partidas([[4,7],[0,0],[0,0],[0,0],[6,0],[9,0],[0,0],[0,0],[0,0],[0,0]])
    assert_equal false, partida.check_rondas()
  end

  def test_una_ronda_con_strike
    partida = creador_de_partidas([[2,7],[10],[0,0],[0,0],[6,0],[9,0],[0,0],[0,0],[0,0],[0,0]])
    assert_equal true, partida.check_strike(partida.rondas[1])
  end

  def test_suma_ronda_con_strike_basico
    partida = creador_de_partidas([[2,7],[10],[6,3],[0,0],[6,0],[9,0],[0,0],[0,0],[0,0],[0,0]])
    assert_equal 52, partida.sumar_puntos()
  end

  def test_una_ronda_con_spare
    partida = creador_de_partidas([[2,7],[7,3],[0,0],[0,0],[6,0],[9,0],[0,0],[0,0],[0,0],[0,0]])
    assert_equal true, partida.check_spare(partida.rondas[1])
  end

  def test_suma_ronda_con_spare_basico
    partida = creador_de_partidas([[2,7],[7,3],[6,3],[0,0],[6,0],[9,0],[0,0],[0,0],[0,0],[0,0]])
    assert_equal 49, partida.sumar_puntos()
  end

  def test_suma_ronda_con_dos_strike_seguidos
    partida = creador_de_partidas([[2,7],[10],[10],[3,2],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]])
    assert_equal 52, partida.sumar_puntos()
  end
  
  def test_suma_ronda_con_tres_strike_seguidos
    partida = creador_de_partidas([[2,7],[10],[10],[10],[3,2],[0,0],[0,0],[0,0],[0,0],[0,0]])
    assert_equal 82, partida.sumar_puntos()
  end

  def test_con_puntos_negativos
    partida = creador_de_partidas([[-2,-7],[10],[10],[10],[3,2],[0,0],[0,0],[0,0],[0,0],[0,0]])
    assert_equal false, partida.sumar_puntos()
  end

  def test_partida_perfecta
    partida = creador_de_partidas([[10],[10],[10],[10],[10],[10],[10],[10],[10],[10],[10,10]])
    assert_equal 300, partida.sumar_puntos()
  end
  
  def test_spare_al_final
    partida = creador_de_partidas([[2,7],[6,3],[6,3],[0,0],[6,0],[9,0],[0,0],[0,0],[0,0],[3,7],[5]])
    assert_equal 57, partida.sumar_puntos()
  end

  def test_partida_todo_esta_mal
    partida = creador_de_partidas([[4],[3],[2],[0],[6],[5],[4],[8],[8],[6],[5]])
    assert_equal false, partida.sumar_puntos()
  end

  def creador_de_partidas(rondas)
    partida = Partida.new rondas
    return partida
  end
  
end