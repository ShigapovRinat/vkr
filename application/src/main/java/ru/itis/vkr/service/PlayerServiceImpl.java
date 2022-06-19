package ru.itis.vkr.service;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import ru.itis.vkr.dto.PlayerDto;
import ru.itis.vkr.model.Player;
import ru.itis.vkr.repository.PlayerRepository;

import java.util.List;
import java.util.stream.Collectors;

@Service
@RequiredArgsConstructor
public class PlayerServiceImpl implements PlayerService {

    private final PlayerRepository repository;

    public List<PlayerDto> getPlayersForTeam(String team, String position) {
        var teamPlayers = repository.findAllByTeamAndPosition(team, position);
        var teamRatingOpt = teamPlayers.stream().mapToDouble(Player::getRating).average();
        return repository.findAllByRatingGreaterThanAndTeamNotLikeAndPosition(teamRatingOpt.orElse(0), team, position)
                .stream()
                .sorted((o1, o2) -> o1.getRating().compareTo(o2.getRating()))
                .limit(10)
                .map(PlayerDto::from)
                .collect(Collectors.toList());
    }
}
