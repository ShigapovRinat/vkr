package ru.itis.vkr.service;

import ru.itis.vkr.dto.PlayerDto;

import java.util.List;

public interface PlayerService {

    List<PlayerDto> getPlayersForTeam(String team, String position);

}
