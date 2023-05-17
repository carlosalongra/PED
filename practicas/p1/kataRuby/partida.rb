class Partida

    attr_accessor :rondas

    def initialize(rondas)
        @rondas = rondas
    end

    def sumar_puntos()
        puntos_totales = 0
        contador_rondas = 0
        rondas_con_ceros = poner_ceros(rondas)
        if !check_rondas()
            return false
        end
        for elemento in rondas_con_ceros
            if check_strike(elemento)
                if check_strike(rondas_con_ceros[contador_rondas]) and contador_rondas == 9
                    puntos_totales = puntos_totales + elemento[0] + suma_strike(contador_rondas, rondas_con_ceros)
                    return puntos_totales
                elsif check_strike(rondas_con_ceros[contador_rondas+1]) 
                    puntos_totales = puntos_totales + elemento[0] + suma_strike(contador_rondas, rondas_con_ceros) + (rondas_con_ceros[contador_rondas+2][0])
                else
                    puntos_totales = puntos_totales + elemento[0] + suma_strike(contador_rondas, rondas_con_ceros)
                end      
            elsif  check_spare(elemento)
                if check_spare(rondas_con_ceros[contador_rondas]) and contador_rondas == 9
                    puntos_totales = puntos_totales + elemento[0] + elemento[1] + suma_spare(contador_rondas, rondas_con_ceros)
                    return puntos_totales
                else
                    puntos_totales = puntos_totales + elemento[0] + elemento[1] + suma_spare(contador_rondas, rondas_con_ceros)
                end  
            else
                puntos_totales = puntos_totales + elemento[0] + elemento[1]
            end
            contador_rondas  = contador_rondas + 1
        end
        return puntos_totales
    end

    def check_rondas()
        rondas_con_ceros = poner_ceros(rondas)
        correctas = 0
        ronda_actual = 0
        for elemento in rondas_con_ceros
            if elemento[0] + elemento[1] <= 10 and elemento[0] >= 0 and elemento[1] >= 0 and ronda_actual < 10
                correctas += 1
            elsif ronda_actual == 10 and !check_spare(rondas_con_ceros[ronda_actual-1]) and !check_strike(rondas_con_ceros[ronda_actual-1])
                return false
            end
            ronda_actual += 1 
        end
        return correctas == 10
    end

    def check_strike(ronda)
        return ronda[0] == 10
    end

    def check_spare(ronda)
        return ronda[0] + ronda[1] == 10
    end

    def suma_strike(ronda_actual, rondas)
        return rondas[ronda_actual+1][0] + rondas[ronda_actual+1][1]
    end

    def suma_spare(ronda_actual, rondas)
        return rondas[ronda_actual+1][0]
    end

    def poner_ceros(rondas)
        for elemento in rondas
            if elemento.length() < 2 
                elemento.push(0)
            end
        end
        return rondas
    end

end