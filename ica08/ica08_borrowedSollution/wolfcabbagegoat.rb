# There is a river with a boat and a bank on each side; that's how rivers work.
# On the left bank is a farmer with their wolf, goat and a cabbage.
# The farmer keeps the peace, they're like a horse whisperer but for goats.
# If the farmer is not around then the goat will eat the cabbage,
# and the wolf will eat the goat. They must not be paired up alone.
# Only the farmer can row the boat; cabbages don't have arms.
# The boat has just 2 spaces because it's cheap, one for farmer one for object.
# The farmer may be in the boat alone but other items must not be left in alone.
# The farmer wants to get all his items to the other bank.

class WGC
    attr_accessor :state
    F, W, G, C = 0, 1, 2, 3

    def initialize(state = nil)
        @start, @goal = [[F, W, G, C], [], []]  ,  [[], [], [F, W, G, C]]
        @state = state || @start[0..-1]
    end

    def won; @state == @goal; end

    def successors
        [[0, 1], [1, 0], [1, 2], [2, 1]].map{ |m| move_source_dest(*m) }.flatten(1)
            .reject{ |p| invalid(p) }.map{ |p| WGC.new(p) }
    end

    def move_source_dest(s, d)
        possibilities = []
        source_orig = @state[s][0..-1]
        if source_orig.include?(WGC::F) # move one
            state = @state[0..-1]
            state[s], state[d] = @state[s][0..-1], @state[d][0..-1]
            state[s].delete(WGC::F)
            state[d].unshift(WGC::F)
            possibilities << state
        end
        if source_orig.include?(WGC::F) && source_orig.size >= 2 # move two
            source_orig.tap{ |o| o.delete(WGC::F) }.size.times do |i|
                state = @state[0..-1]
                state[s], state[d] = source_orig[0..-1], @state[d][0..-1]
                state[d].push(WGC::F).push(state[s].delete_at(i)).sort!
                possibilities << state
            end
        end
        possibilities
    end

    def invalid(s)
        # boat has two max
        return true if s[1].size > 2
        3.times do |i|
            # goat must not be left alone with cabbage
            return true if s[i].include?(WGC::G) && s[i].include?(WGC::C) &&
                !s[i].include?(WGC::F)
            # wolf must not be left alone with goat
            return true if s[i].include?(WGC::W) && s[i].include?(WGC::G) &&
                !s[i].include?(WGC::F)
        end
        false
    end
end


class Run
    def initialize; @history, @won = [], false; end

    def go(problem)
        onwards(problem, 0)
        @history
    end

    def onwards(problem, depth)
        @history << problem.state
        unless @won = problem.won
            problem.successors.each do |s|
                unless @won
                    @history = @history[0..depth]
                    onwards(s, depth+1) unless @history.include?(s.state)
                end
            end
        end
    end
end


class WGCPrinter
    def initialize(file)
        @symbols = File.read(file).split("\n\n").map{ |s| s.split("\n").reverse() }
    end

    def width(symbol); symbol.map{ |line| line.size }.max; end

    def total_width; @symbols.map{ |s| width(s) + 2 }.inject(&:+); end

    def max_height; @symbols.map{ |s| s.size }.max; end

    def print_state(state)
        (-1..max_height).map do |i| # each row of ascii prints out
            (0..state.size-1).map do |p| # position of the state (bank, boat...)
                g = (i == -1 || i == max_height) && (p != 0 && p != state.size-1) ? '-' : ' '
                pos = state[p].map do |sym| # symbol in the position (wolf, goat...)
                    s = @symbols[sym]
                    g + ((s && i!=-1 && s[i]) || '').ljust(width(s), g) + g
                end.join
                row = g * (total_width - pos.size) + pos
                br = i==0 ? '/' : (i==max_height-1 ? '\\' : (i==-1 || i==max_height ? '~' : '|'))
                bl = i==0 ? '\\' : (i==max_height-1 ? '/' : (i==-1 || i==max_height ? '~' : '|'))
                row += br + "~(" if p == state.size-2
                row += ")~" + bl if p == 0
                row
            end.join
        end.reverse.each{ |l| puts l }
    end
end


printer = WGCPrinter.new('wgc_ascii.txt')
Run.new.go(WGC.new).each{ |s| printer.print_state(s) }


#Run.new.go(WGC.new).each{ |s| p s }